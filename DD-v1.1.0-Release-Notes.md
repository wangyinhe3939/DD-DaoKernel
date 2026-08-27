# DD-DaoKernel v1.1.0 — Contracts, Evals and Portability

v1.1.0 turns DD-DaoKernel from a governance idea into a more testable engineering contract.

## Added

- Skill Contract JSON Schema
- Agent Contract JSON Schema
- Positive / negative / failure fixtures for all 8 core Skills
- GitHub Actions validation workflow
- Codex / Claude / Gemini compatibility guidance
- Full English README
- 6 real-world examples
- CONTRIBUTING.md
- SECURITY.md
- Standard operational Trace example

## Core behavior unchanged

The kernel remains:

`Evidence → Name → Desire → Arena → Action → Autonomy → Stop → Boundary`

And preserves:

- maximum 3 DD Skills per task;
- one writer per execution stage;
- minimum permissions;
- explicit rollback;
- HUMAN gate for high-risk actions;
- STOP when acceptance criteria are met.

## Breaking changes

None intended.

v1.1.0 adds contracts and validation around the existing design rather than replacing it.
