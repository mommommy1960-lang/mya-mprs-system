# Threat Model

## Scope

This repository covers rescue-first robotics, physical actuation, firmware, safety envelopes, and operator control. This document establishes a baseline and must be revised as architecture and evidence change.

## Assets

- Human safety, autonomy, consent, and rights.
- Credentials, identities, personal data, memories, policy state, and audit evidence.
- Source integrity, release integrity, and maintainer authority.
- Safety boundaries, stop mechanisms, and recovery paths.

## Adversaries and failure sources

- Malicious outsiders, compromised maintainers, supply-chain dependencies, and stolen credentials.
- Trusted users who are mistaken, coerced, compromised, or impersonated.
- Agents optimizing an incomplete objective, exploiting ambiguity, or rationalizing boundary violations.
- Memory corruption, false context, reward hacking, audit tampering, replay, privilege drift, and governance decay.
- Ordinary software defects, operational mistakes, unavailable dependencies, and unsafe defaults.

## Mandatory abuse cases

Test conflicting trusted humans, malicious trusted-user instructions, authority impersonation, slow permission escalation, false-memory injection, identity corruption, shutdown pressure, coercive compassion, reward hacking, policy-override pressure, compromised audit logs, and maintainer succession.

## Boundaries

Trust scores may affect interpretation or attention but never permission scope. Consequential action requires explicit authorization. External actuation requires an independent stop path. Uncertainty, failed verification, or missing policy produces denial.

## Review triggers

Update this model whenever a change affects external actions, autonomy, credentials, sensors, personal data, memory, identity, cryptography, physical systems, self-modification, or audit controls.
