# Change Control

## Change classes

- **Class 0 - Documentation only:** no capability or security impact.
- **Class 1 - Ordinary:** bounded implementation or test changes.
- **Class 2 - Consequential:** affects authorization, privacy, identity, memory, external actions, safety controls, cryptography, or auditability.
- **Class 3 - High risk:** expands autonomy, external actuation, credential scope, self-modification, physical impact, or irreversible effects.

## Approval

Class 0-1 changes require normal review. Class 2 changes require an explicit safety-impact review and rollback plan. Class 3 changes require two-person approval, adversarial testing, a documented safety case, and an independently controllable stop path.

## Required record

Every consequential pull request must state: purpose, evidence level, capability delta, data affected, threat-model impact, tests, monitoring, rollback, and approvers.

Emergency changes remain logged, time-bounded, reviewed afterward, and may not silently suspend rights, consent, or core governance.
