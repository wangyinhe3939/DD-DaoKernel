# DD-DaoKernel v1.1.0 实施清单

名称：DD-DaoKernel v1.1.0 Hardening
类型：Workflow + Eval + Adapter + Contract
解决的问题：把已有治理思想升级为机器可读、可验证、可移植、可贡献的工程版本。
触发条件：v1.0.0 已存在 8 Skills / 4 Agents，但缺少契约、测试、CI、适配和发布工程。
非触发条件：不新增第 9 个核心 Skill；不重构现有哲学；不创建新业务 Agent。
输入：v1.0.0 仓库结构与现有治理规则。
输出：2 个 Contract Schema、8×3 测试、CI、兼容说明、英文 README、6 案例、贡献与安全文档、Trace、Release Notes。
工具：GitHub / Python validator / GitHub Actions。
权限：仓库分支写入、PR、Release；不需要生产系统、密钥或外部业务权限。
风险等级：MEDIUM。
人工确认点：合并到 main 与发布正式 Release。
交接对象：仓库维护者。
验证方式：`python scripts/DD-验证v1_1_0.py` + GitHub Actions PASS。
回滚方式：Revert v1.1.0 PR / tag。
停止条件：10 项全部落地、CI PASS、Release 建立。
支持平台：Codex / Claude / Gemini / Generic。
已知限制：当前 GitHub 集成阻止创建分支，无法在本会话直接完成远端提交与 Release。
测试案例：8 个 Skill 各含 positive / negative / failure。
当前不做：新增核心 Skill、Agent Console、复杂网络多 Agent、生产自动化。
