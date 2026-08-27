# Security Policy

DD-DaoKernel 处理的是 Agent 的决策、权限与执行边界，因此安全问题不仅包括传统代码漏洞，也包括越权和错误自动化。

## 不应公开提交的内容

- API keys / tokens / passwords
- 私人记忆
- 客户数据
- 真实聊天记录
- 生产数据库内容
- 生产配置
- 私有案件、身份或财务资料
- 任何未脱敏的凭证

## 高风险行为

以下行为默认需要人工确认：
- DELETE
- OVERWRITE
- PUBLISH
- SEND
- PAY
- PERMISSION_CHANGE
- PRODUCTION_DEPLOY
- DATA_MIGRATION
- SECRET_ACCESS

## Agent 安全边界

Agent 不得：
- 自行扩权
- 修改核心治理指令来绕过限制
- 创建不受监管的新写入者
- 绕过 VETO
- 将 UNKNOWN 伪装成 VERIFIED
- 在没有停止条件时持续执行

## 漏洞报告

请不要在公开 Issue 中粘贴密钥、生产数据或私人资料。

报告应最少包含：
1. 受影响组件
2. 复现条件
3. 最大影响面
4. 是否可逆
5. 建议的临时缓解方式

优先目标是缩小 blast radius，而不是证明漏洞有多“酷”。
