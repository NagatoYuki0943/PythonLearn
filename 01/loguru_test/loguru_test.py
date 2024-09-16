"""
https://zhuanlan.zhihu.com/p/429452898
https://zhuanlan.zhihu.com/p/681344797

日志级别:
    Trace：   这个级别用于记录非常详细的信息，通常用于调试，以便开发者能够追踪程序的每一个步骤。Trace 级别通常用于开发过程中，生产环境中很少使用。
    Debug：   Debug 级别用于记录程序的运行细节，帮助开发者理解程序的行为。它比 Trace 级别稍微宽泛一些，但仍然非常详细。
    Info：    Info 级别用于记录程序的正常运行情况，例如程序启动、配置信息、用户操作等。它提供了程序运行状态的一般信息。
    Success： Success 级别用于记录程序中成功完成的操作，如任务完成、操作成功等。它通常用于表示一个操作或请求的成功结果。
    Warning： Warning 级别用于记录那些可能不是错误，但可能会引起问题的情况。例如，资源不足、配置错误等，需要用户注意但不影响程序继续运行。
    Error：   Error 级别用于记录程序中的错误，这些错误可能会导致程序的某些功能无法正常工作，但通常不会导致程序崩溃。
    Critical：Critical 级别用于记录非常严重的错误，这些错误可能会导致程序崩溃或数据丢失。在这种情况下，程序可能需要立即采取行动或停止运行。


add 完整参数:
    Loguru 对输出到文件的配置有非常强大的支持，比如支持输出到多个文件，分级别分别输出，过大创建新文件，过久自动删除等等。

    基本语法:
        add(sink, *, level='DEBUG', format='<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>', filter=None, colorize=None, serialize=False, backtrace=True, diagnose=True, enqueue=False, catch=True, **kwargs)

    基本参数释义:
        sink: 可以是一个 file 对象，例如 sys.stderr 或 open('file.log', 'w')，也可以是 str 字符串或者 pathlib.Path 对象，即文件路径，也可以是一个方法，可以自行定义输出实现，也可以是一个 logging 模块的 Handler，比如 FileHandler、StreamHandler 等，还可以是 coroutine function，即一个返回协程对象的函数等。
        level: 日志输出和保存级别。
        format: 日志格式模板。
        filter: 一个可选的指令，用于决定每个记录的消息是否应该发送到 sink。
        colorize: 格式化消息中包含的颜色标记是否应转换为用于终端着色的 ansi 代码，或以其他方式剥离。 如果没有，则根据 sink 是否为 tty（电传打字机缩写） 自动做出选择。
        serialize: 在发送到 sink 之前，是否应首先将记录的消息转换为 JSON 字符串。
        backtrace: 格式化的异常跟踪是否应该向上扩展，超出捕获点，以显示生成错误的完整堆栈跟踪。
        diagnose: 异常跟踪是否应显示变量值以简化调试。建议在生产环境中设置 False，避免泄露敏感数据。
        enqueue: 要记录的消息是否应在到达 sink 之前首先通过多进程安全队列，这在通过多个进程记录到文件时很有用，这样做的好处还在于使日志记录调用是非阻塞的。
        catch: 是否应自动捕获 sink 处理日志消息时发生的错误，如果为 True，则会在 sys.stderr 上显示异常消息，但该异常不会传播到 sink，从而防止应用程序崩溃。
        kwargs: 仅对配置协程或文件接收器有效的附加参数（见下文）。

    当且仅当 sink 是协程函数时，以下参数适用:
        loop: 将在其中调度和执行异步日志记录任务的事件循环。如果为 None，将使用 asyncio.get_event_loop() 返回的循环。

    当且仅当 sink 是文件路径时，以下参数适用:
        rotation: 一种条件，指示何时应关闭当前记录的文件并开始新的文件。
        retention: 过滤旧文件的指令，在循环或程序结束期间会删除旧文件。
        compression: 日志文件在关闭时应转换为的压缩或存档格式。
        delay: 是在配置 sink 后立即创建文件，还是延迟到第一条记录的消息时再创建。默认为 False。
        mode: 内置 open() 函数的打开模式，默认为 a（以追加模式打开文件）。
        buffering: 内置 open() 函数的缓冲策略，默认为1（行缓冲文件）。
        encoding: 内置 open() 函数的文件编码，如果 None，则默认为 locale.getpreferredencoding()。
        kwargs: 其他传递给内置 open() 函数的参数。

    rotation 参数，可以实现按照固定时间创建新的日志文件
        设置每天 0 点新创建一个 log 文件:
            logger.add('runtime_{time}.log', rotation='00:00')

        设置超过 100 MB 新创建一个 log 文件:
            logger.add('runtime_{time}.log', rotation="100 MB")

        设置每隔一个周新创建一个 log 文件:
            logger.add('runtime_{time}.log', rotation='1 week')

        设置日志文件最长保留 15 天:
            logger.add('runtime_{time}.log', retention='15 days')

        设置日志文件最多保留 10 个:
            logger.add('runtime_{time}.log', retention=10)

        可以是一个 datetime.timedelta 对象，比如设置日志文件最多保留 5 个小时:
            import datetime
            from loguru import logger

            logger.add('runtime_{time}.log', retention=datetime.timedelta(hours=5))

    compression 参数，可以配置日志文件的压缩格式，这样可以更加节省存储空间，比如设置使用 zip 文件格式保存:
        logger.add('runtime_{time}.log', compression='zip')

        其格式支持: gz、bz2、xz、lzma、tar、tar.gz、tar.bz2、tar.xz
"""

from loguru import logger


# 将日志输出到文件
# 每天 0 点新创建一个 log 文件
log_file = logger.add("runtime_{time}.log", rotation="00:00")


# Loguru 提供七个独特的日志级别
logger.trace("A trace message.")  # trace 不会输出
logger.debug("A debug message.")
logger.info("An info message.")
logger.success("A success message.")
logger.warning("A warning message.")
logger.error("An error message.")
logger.critical("A critical message.")


# 也可以使用 remove() 方法移除指定的日志文件
# 不会删除文件,而是不再写入这个文件
logger.remove(log_file)


# 这个日志没有写入到文件，只是在屏幕上打印
logger.critical("Another a critical message.")
