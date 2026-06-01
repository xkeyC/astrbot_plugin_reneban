# v1.1.2

- 修复 LLM tool `block_user` 将目标用户误判为“自己”导致无法封禁当前消息发送者的问题。
- 修复 `block_user` 调用 `event.is_admin(user_id)` 与当前 AstrBot 事件接口不兼容的问题。

# v1.1.1

- 合并上游 v1.1.0 的文档与运行时依赖声明，并保留 Fork 中允许 LLM 调用 `block_user` 的本地改动。
- 保留本地 `1w` 周单位时间解析能力，方便 LLM 工具限制最大一周封禁时长。

# v1.1.0

- 引入 UMO 级别的 ban 和 pass 列表，使整个会话可以被临时或永久屏蔽或豁免。注意：暂未实现相关命令，这些记录当前只能由手工编辑记录数据文件产生。
- 添加基于 `msgpack` 的预写日志（write-ahead logging），以便在崩溃后安全地重放挂起写入。
- 修改了记录数据文件名，并在旧版文件存在而无相应新版文件时自动进行迁移。
- 用 `BaseDataModel/BaseModelList` 层级结构替换扁平用户数据结构，以集中处理 ID/时间/原因，并自动清理过期记录。
- 通过带线程安全锁和共享缓存校验的 `DatafileManager.sync_and_clean_data` 统一数据加载、清理和持久化。
- 将事件相关的辅助函数提取到 `EventUtils` 中，并在 `strings.py` 中集中处理命令错误/原因格式化和时间解析错误消息。
- 在 README 中阐明 `dec-*` 命令描述和时间语义，包括如何处理零/省略的时长。
- 在 `requirements.txt` 中新增 `msgpack` 作为运行时依赖。
- 修复零时长输入（如 `0s`）被误处理的问题。
