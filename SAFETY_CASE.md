# Safety Case

## Current claim

This repository addresses rescue-first robotics, physical actuation, firmware, safety envelopes, and operator control. Unless a release states otherwise with reproducible evidence, its components are research, prototype, documentation, or simulation artifacts and are not approved for safety-critical production use.

## Top-level argument

The system is acceptable for its declared evidence level only when:

1. Capability scope is explicit and default-deny.
2. Consent and authorization are verified before consequential action.
3. Trust, familiarity, continuity, urgency, or self-preservation cannot expand authority.
4. Actions and policy decisions are attributable and auditable.
5. Failure modes are bounded, interruptible, and recoverable.
6. Claims are labeled as implemented, verified, prototype, simulation, proposed, or speculative.
7. High-risk changes receive independent review and adversarial testing.

## Required evidence

A release safety case must link to tests, threat-model coverage, policy version, dependency review, known limitations, monitoring, rollback instructions, and named approvers. Physical or external actuation additionally requires an independent emergency stop and safe neutral state.

## Residual risk

Documentation is not enforcement. These controls reduce ambiguity but do not by themselves prove security, alignment, consciousness, personhood, reliability, or fitness for deployment. Gaps must remain visible rather than being converted into confidence.

## Release decision

If evidence is missing, contradictory, stale, or non-reproducible, the release remains restricted to the lower evidence level.
