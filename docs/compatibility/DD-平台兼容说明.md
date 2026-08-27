# DD-DaoKernel 平台兼容说明

## 核心原则

DD-DaoKernel 的核心契约不绑定任何单一模型厂商。

核心层只定义：
- 决策规则
- Skill Contract
- Agent Contract
- 输入 / 输出
- 权限边界
- 人工确认点
- 验收、回滚与停止条件

平台特定格式只属于 Adapter。

## Codex

当前原生适配最完整。

- 项目级规则：`AGENTS.md`
- Skills：`.agents/skills/<skill>/SKILL.md`
- Agents：`.codex/agents/*.toml`
- 推荐：由 `DD-道枢总控` 负责路由，单任务最多激活 3 个 DD Skills。
- 写入阶段最多 1 个写入者。
- 高风险动作交给 `DD-守中监察` 做 GO / GO WITH CONDITIONS / STOP / HUMAN 判断。

## Claude

兼容方式：
- 将 `AGENTS.md` 核心治理规则映射到项目级 Claude instructions。
- 将每个 `SKILL.md` 作为按需加载的方法模块。
- Agent 权限、交接、停止条件以 `DD-agent-contract.schema.json` 为平台无关真源。
- Claude 特有配置不得反写进入核心契约。

限制：
- 不假设 Claude 一定支持 Codex TOML Agent 格式。
- 不把平台专属 tool 名称写进 Skill 核心逻辑。

## Gemini

兼容方式：
- 将治理规则映射到项目/系统级 instruction。
- Skills 作为独立上下文模块按触发条件加载。
- Tool calling 仅作为 Adapter 层实现。
- 保持 VERIFIED / ASSUMPTION / UNKNOWN 标记与 STOP / HUMAN 终止语义。

限制：
- Gemini 的工具名、配置字段和运行容器可能与 Codex 不同。
- 平台能力 UNKNOWN 时不得假装兼容。

## Generic

任何支持“系统指令 + 工具调用 + 状态/消息传递”的 Agent Runtime，都可以实现：
`Evidence → Name → Desire → Arena → Action → Autonomy → Stop → Boundary`

最低兼容要求：
1. 能区分读与写。
2. 能限制 Tool 权限。
3. 能保留停止条件。
4. 能在 HIGH 风险时要求人工确认。
5. 能记录最小 Trace。

## 兼容性原则

`Core Contract > Adapter > Vendor Configuration`

厂商变化时只替换 Adapter。
不要让平台格式污染 Kernel。
