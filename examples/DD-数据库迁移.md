# DD-数据库迁移

问题：需要修改生产数据库结构。

分类：Workflow / HIGH。

界：要求迁移前备份、dry-run、向后兼容检查、回滚 SQL、人工确认。

单写入者：执行阶段只能由一个 Writer 进行迁移。

验：schema、读写路径、回滚演练全部通过。

停止：任一关键 UNKNOWN 无法消除则 HUMAN；发生异常立即 ROLLBACK。
