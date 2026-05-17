# new_event_loop, set_event_loop, get_running_loop 现代场景

# 场景2:
# Python 3.12 以后，asyncio.run() 和 asyncio.Runner 支持 loop_factory。
# 文档还特别说，推荐用 loop_factory 配置事件循环，而不是 policy；而且 Runner 的 loop_factory 有责任把创建出来的 loop 设置成 current loop。


import asyncio


def loop_factory():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    return loop


async def main():
    print(asyncio.get_running_loop())
    # <ProactorEventLoop running=True closed=False debug=False>


with asyncio.Runner(loop_factory=loop_factory) as runner:
    runner.run(main())
