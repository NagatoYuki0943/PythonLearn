# asyncio.new_event_loop()
# 创建一个新的事件循环对象。

# 但它只是 创建，不会自动运行，也不一定自动变成当前线程的事件循环。官方定义就是 “Create and return a new event loop object”。
# 常见用途：
#   在 非主线程 里创建事件循环。
#   自己写框架/测试工具，需要手动控制 loop 生命周期。
#   给 asyncio.Runner(loop_factory=...) 或 asyncio.run(..., loop_factory=...) 提供自定义 loop。
#   集成特殊事件循环实现，比如 uvloop，虽然现在更推荐通过 loop_factory，不是旧的 policy 机制。


import asyncio


loop = asyncio.new_event_loop()
print(loop)  # <ProactorEventLoop running=False closed=False debug=False>
