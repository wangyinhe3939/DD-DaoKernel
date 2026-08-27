# DD-DaoKernel

> A decision kernel for coding agents.

**The goal is not to make an agent do more.  
The goal is to keep it from taking the extra step that creates more problems than it solves.**

`Evidence → Name → Desire → Arena → Action → Autonomy → Stop → Boundary`

## Why

Modern coding agents can act even when requirements are unclear, facts are unverified, scope is drifting, or the task is already complete.

DD-DaoKernel adds operational constraints:

- separate facts from assumptions and unknowns;
- challenge the problem framing before changing code;
- remove goal pollution;
- reject the wrong battlefield;
- choose the minimum sufficient intervention;
- reduce unnecessary actor dependency;
- stop when marginal gain no longer beats reverse risk;
- inspect permission, reversibility, blast radius and external side effects.

## Quick Start

```bash
git clone https://github.com/wangyinhe3939/DD-DaoKernel.git
cd DD-DaoKernel
```

Core layout:

```text
.agents/skills/      8 decision skills
.codex/agents/       4 separated agent powers
contracts/           machine-readable contracts
tests/skills/        positive / negative / failure fixtures
docs/compatibility/  platform adapters guidance
docs/trace/          standard trace example
examples/            real-world cases
AGENTS.md             project governance
```

Run validation:

```bash
python scripts/DD-验证v1_1_0.py
```

## Eight Skills

| Core | Skill | Purpose |
|---|---|---|
| Evidence | `dd-evidence` | Verify decision-critical claims |
| Name | `dd-name` | Challenge labels, framing and proposed solutions |
| Desire | `dd-desire` | Remove goal pollution |
| Arena | `dd-arena` | Reject the wrong path or objective function |
| Action | `dd-min-action` | Find the minimum sufficient intervention |
| Autonomy | `dd-autonomy` | Reduce unnecessary actor dependency |
| Stop | `dd-stop` | Detect diminishing returns and second-order risk |
| Boundary | `dd-boundary` | Review permissions, reversibility and blast radius |

A single task should not activate every skill. The default maximum is three DD Skills.

## Four Powers

DD-DaoKernel separates powers instead of inventing personalities.

### DD-道枢总控 — DECISION

Routes the task, selects the necessary skills, defines the next action and stops scope drift.

### DD-观道参谋 — READ

Observes facts, blind spots, hidden assumptions, counterfactuals and second-order effects. It does not write.

### DD-行水执行 — WRITE

Executes the smallest reversible and verifiable patch. One execution stage has at most one writer.

### DD-守中监察 — VETO

Reviews risk, authority, irreversibility, blast radius, rollback and stop conditions.

Outputs:

`GO / GO WITH CONDITIONS / STOP / HUMAN`

## Governance Rules

- Evidence before conclusion.
- UNKNOWN stays UNKNOWN.
- A solution is not the goal.
- One execution stage has at most one writer.
- Default to minimum permissions and minimum blast radius.
- High-risk external side effects require human approval.
- Do not expand scope because something is convenient to fix.
- Do not create agents merely to show capability.
- Do not let agents expand their own authority.
- Every automation needs a human handoff and an exit path.
- Stop immediately when acceptance criteria are met.

## Skill Contract

v1.1.0 introduces a machine-readable Skill Contract schema.

A conforming skill defines:
- purpose;
- trigger and non-trigger conditions;
- inputs and outputs;
- required tools;
- allowed permissions;
- risk level;
- human gate;
- success criteria;
- rollback;
- stop condition;
- known limitations;
- supported platforms.

See `contracts/DD-skill-contract.schema.json`.

## Agent Contract

A conforming agent additionally defines:
- responsibility;
- authority;
- forbidden authority;
- state;
- handoff;
- available skills and tools;
- veto relationships.

See `contracts/DD-agent-contract.schema.json`.

## Testing

Each of the eight core Skills includes three fixture types:

- **Positive** — the skill should trigger.
- **Negative** — the skill should stay out.
- **Failure** — the skill cannot safely complete and must expose UNKNOWN, STOP, ROLLBACK or HUMAN instead of inventing certainty.

The v1.1.0 CI checks the contracts, fixtures, documentation, trace and example count.

## Trace

A standard trace records:

`input → evidence → decision → action → verification → boundary → stop`

The trace is not a hidden chain of thought. It is an operational audit record: claims, permissions, actions, tests and stop decisions.

See `docs/trace/DD-标准Trace示例.json`.

## Platform Compatibility

The core contract is vendor-neutral.

- Codex currently has the most direct adapter through `AGENTS.md`, `.agents/skills/` and `.codex/agents/`.
- Claude can map the same contracts into project instructions, skills and tool permissions.
- Gemini can map the same contracts into instructions and tool adapters.
- Vendor-specific fields belong in Adapter layers, never in the core contract.

See `docs/compatibility/DD-平台兼容说明.md`.

## When Not to Use It

Do not invoke the full kernel for:
- changing one color;
- replacing one sentence;
- formatting a file;
- a fully specified one-line bug.

If governance creates more complexity than the task itself, governance should step out.

## Security

High-risk actions such as deletion, publishing, production deployment, permission changes, money movement, data migration or secret access require explicit boundaries and normally require human approval.

See `SECURITY.md`.

## Contributing

A contribution must explain the real problem, trigger, non-trigger, permissions, tests, rollback and stop condition.

See `CONTRIBUTING.md`.

## License

MIT.
