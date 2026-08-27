# Contributing to DD-DaoKernel

感谢参与。

这个项目不是 Agent / Prompt 收藏夹。任何贡献都必须证明它解决了一个真实问题，并且有明确边界。

## 提交前先分类

`Kernel / Skill / Agent / Tool / Workflow / Adapter / Eval`

没有独立权限、状态或交接需求，不要创建 Agent，优先做 Skill。

## 新 Skill 最低要求

必须包含：
- 真正问题
- Trigger
- Non-trigger
- Inputs / Outputs
- Required tools
- Minimum permissions
- Risk level
- Human gate
- Success criteria
- Rollback
- Stop condition
- Known limitations
- Positive / Negative / Failure tests

## 新 Agent 最低要求

除了以上内容，还必须回答：
- 为什么必须独立存在
- 有什么 authority
- 明确没有什么 authority
- 状态由谁维护
- 向谁 handoff
- 谁可以 veto
- 什么时候必须交还给 HUMAN

## 禁止

- 为展示能力增加 Agent
- 无测试的“智能化”
- 自行扩权
- 把 UNKNOWN 写成事实
- 单阶段多个写入者
- 无停止条件的循环
- 把 Codex / Claude / Gemini 特定格式写进核心 Contract

## PR 验证

提交前运行：

```bash
python scripts/DD-验证v1_1_0.py
```

必须 PASS。

## 变更原则

最小补丁。
可验证。
可回滚。
达到验收条件立即停止。
