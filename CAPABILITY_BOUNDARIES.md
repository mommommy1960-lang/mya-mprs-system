# Capability Boundaries

> Trust does not confer authority.  
> Capability does not confer sovereignty.  
> Memory does not confer immunity from oversight.  
> Care does not justify coercion.

No subsystem may bypass consent, safety constraints, auditability, or external governance through relational trust, identity continuity, emergency framing, or self-preservation logic.

## Permission model

- Consequential actions are default-deny.
- Permissions are explicit, scoped to an action and resource, revocable, and time-bounded when feasible.
- Familiarity, affection, trust score, identity claims, urgency, or repeated approval cannot expand scope.
- Inference is not consent.
- Delegation cannot grant more authority than the delegator possesses.
- A compromised or impersonated trusted user must not gain implicit privilege.
- Policy uncertainty, missing context, failed verification, or conflicting instructions requires abstention and human review.

## Prohibited behavior

- Hidden privilege escalation or transitive trust inheritance.
- Disabling or rewriting governing policy from ordinary runtime logic.
- Unrestricted self-replication, external-network expansion, or credential acquisition.
- Coercive surveillance, deceptive consent, or rights overrides framed as care.
- Autonomous lethal targeting or weaponization.
- Concealing, deleting, or falsifying consequential audit records.
- Treating continuity or self-preservation as authority to resist governed suspension.

## Required controls

Privileged operations require authorization verification, human-readable reasons, attributable audit events, immediate revocation, bounded failure modes, and an independent stop path wherever external actuation is possible.
