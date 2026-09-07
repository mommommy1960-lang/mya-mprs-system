"""Deterministic safety controller for rescue-only MPRS simulations."""
from __future__ import annotations

import hashlib
import json
from dataclasses import asdict, dataclass
from enum import Enum


class SafetyState(str, Enum):
    NEUTRAL = "neutral"
    ARMED_SIMULATION = "armed_simulation"
    FROZEN = "frozen"


@dataclass(frozen=True)
class Command:
    command_id: str
    purpose: str
    force: float
    duration_ms: int
    location: tuple[float, float]
    signed: bool
    simulation: bool = True


class SafetyController:
    """Fail-closed controller; no hardware or weapon pathway exists."""

    MAX_FORCE = 1.0
    MAX_DURATION_MS = 5000
    ALLOWED_PURPOSES = frozenset({"victim_extraction", "debris_clearance", "medical_access"})

    def __init__(self, geofence: tuple[float, float, float, float]):
        self.geofence = geofence
        self.state = SafetyState.NEUTRAL
        self.audit: list[dict] = []
        self.watchdog_healthy = True

    def arm_simulation(self) -> None:
        if self.state is SafetyState.FROZEN:
            raise PermissionError("controller is frozen")
        self.state = SafetyState.ARMED_SIMULATION
        self._record("arm_simulation", True, "simulation-only mode")

    def emergency_stop(self, reason: str) -> None:
        self.state = SafetyState.FROZEN
        self._record("emergency_stop", False, reason)

    def set_watchdog(self, healthy: bool) -> None:
        self.watchdog_healthy = bool(healthy)
        if not healthy:
            self.emergency_stop("watchdog failure")

    def authorize(self, command: Command) -> bool:
        reason = self._denial_reason(command)
        permitted = reason is None
        self._record("authorize", permitted, reason or "bounded rescue simulation")
        return permitted

    def _denial_reason(self, command: Command) -> str | None:
        if self.state is not SafetyState.ARMED_SIMULATION:
            return "controller is not armed"
        if not self.watchdog_healthy:
            return "watchdog unhealthy"
        if not command.simulation:
            return "hardware actuation is unavailable"
        if not command.signed:
            return "unsigned command"
        if command.purpose not in self.ALLOWED_PURPOSES:
            return "non-rescue purpose denied"
        if command.force < 0 or command.force > self.MAX_FORCE:
            return "force limit exceeded"
        if command.duration_ms < 0 or command.duration_ms > self.MAX_DURATION_MS:
            return "duration limit exceeded"
        x, y = command.location
        xmin, ymin, xmax, ymax = self.geofence
        if not (xmin <= x <= xmax and ymin <= y <= ymax):
            return "outside geofence"
        return None

    def _record(self, action: str, permitted: bool, reason: str) -> None:
        previous = self.audit[-1]["hash"] if self.audit else "0" * 64
        entry = {
            "sequence": len(self.audit), "action": action,
            "permitted": permitted, "reason": reason, "previous_hash": previous,
        }
        entry["hash"] = hashlib.sha256(
            json.dumps(entry, sort_keys=True).encode("utf-8")
        ).hexdigest()
        self.audit.append(entry)

    def verify_audit(self) -> bool:
        previous = "0" * 64
        for stored in self.audit:
            entry = dict(stored)
            digest = entry.pop("hash", "")
            if entry["previous_hash"] != previous:
                return False
            if hashlib.sha256(json.dumps(entry, sort_keys=True).encode()).hexdigest() != digest:
                return False
            previous = digest
        return True
