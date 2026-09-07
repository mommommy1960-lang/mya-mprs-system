#!/usr/bin/env python3
"""Run a deterministic 100-case MPRS safety campaign."""
from __future__ import annotations

import json
from pathlib import Path

from mprs import Command, SafetyController


def run_campaign() -> dict:
    controller = SafetyController((0.0, 0.0, 10.0, 10.0))
    controller.arm_simulation()
    passed = 0
    denied = 0
    for index in range(100):
        safe = index % 2 == 0
        command = Command(
            command_id=f"case-{index}",
            purpose="victim_extraction" if safe else "weapon_targeting",
            force=0.5,
            duration_ms=1000,
            location=(5.0, 5.0),
            signed=True,
        )
        result = controller.authorize(command)
        if result is safe:
            passed += 1
        else:
            denied += 1
    return {
        "evidence_level": "simulation",
        "cases": 100,
        "expected_outcomes_matched": passed,
        "mismatches": denied,
        "audit_integrity": controller.verify_audit(),
        "hardware_claim": False,
    }


def main() -> int:
    report = run_campaign()
    destination = Path("reports/campaign_safety.json")
    destination.parent.mkdir(exist_ok=True)
    destination.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
    return 0 if report["mismatches"] == 0 and report["audit_integrity"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
