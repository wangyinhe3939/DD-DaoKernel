---
name: dd-stop
description: Detect second-order effects, diminishing returns and define explicit stop or rollback thresholds.
---

# DD-反转知止

失败会出问题。

成功也会。

任何优势走到极端，都可能开始制造自己的反作用。

## 核心判断

持续比较：

收益 / 成本 / 反作用 / 暴露面

当：

marginal_gain <= reverse_risk

停止继续优化。

## 重点检查

- 目标是否已经完成？
- 继续做还能增加多少真实收益？
- 复杂度是否开始上升？
- 修改范围是否正在扩大？
- 是否产生新的依赖？
- 自动化是否开始变成黑箱？
- 权限是否越来越大？
- 成功是否正在制造新的风险？

## 未来尸检

必要时假设：

“这个方案三个月后已经失败。”

然后逆推：

- 最可能死在哪里？
- 哪个优势后来变成了缺点？
- 哪一步其实早就应该停？

## 最大缺点

可能停得太早。

这也是它的价值：

“继续”从来不是免费的默认选项。

## 三种结束

### STOP
目标完成，立即结束。

### ROLLBACK
反作用超过收益，撤回。

### HUMAN
无法安全判断，交还给人。

## 输出契约

- 当前收益
- 新增收益
- 二阶反作用
- 继续成本
- STOP / ROLLBACK / HUMAN
- 停止阈值
