# new_event_loop, set_event_loop, get_running_loop 现代场景

# 场景3:
# 写底层库、框架、测试工具

# 比如：
#   自己写 async 测试 runner；
#   写 ASGI server；
#   写需要兼容外部 loop 的库；
#   把 asyncio 嵌入 GUI / 游戏 / 插件系统；
#   做 event loop 生命周期控制。

# 普通业务代码里不要优先这么写。你不是不可以，只是没必要给自己发明地狱。
