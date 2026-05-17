# asyncio.get_event_loop()
# 获取当前事件循环。
#   loop = asyncio.get_event_loop()
# 但这个函数现在有点危险，因为它的行为历史包袱很重。
# 在 coroutine 或 callback 里调用时，它会返回当前正在运行的 loop；如果没有正在运行的 loop，它会尝试从 event loop policy 里拿当前 loop。
# Python 3.14 开始，如果没有 current event loop，会直接抛 RuntimeError。
# 官方也明确说，在 coroutine 和 callback 里更推荐用 get_running_loop()，因为 get_event_loop() 行为更复杂。
# 所以现在更推荐：
#   loop = asyncio.get_running_loop()
# 尤其不要在同步顶层代码里写：
#   loop = asyncio.get_event_loop()
#   loop.run_until_complete(main())
# 这属于 asyncio 旧时代样板代码，像 C++ 里手搓内存管理一样充满仪式感和隐患。
