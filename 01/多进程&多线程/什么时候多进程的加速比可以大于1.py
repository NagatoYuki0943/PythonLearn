def parallel_apply(func, iterable, workers, max_queue_size, callback=None, dummy=False):
    """多进程或多线程地将func应用到iterable的每个元素中。
    注意这个apply是异步且无序的，也就是说依次输入a,b,c，但是
    输出可能是func(c), func(a), func(b)。
    参数：
        dummy: False是多进程/线性，True则是多线程/线性；
        callback: 处理单个输出的回调函数；
    """
    if dummy:
        from multiprocessing.dummy import Pool, Queue
    else:
        from multiprocessing import Pool, Queue
    import queue

    in_queue, out_queue = Queue(max_queue_size), Queue()

    def worker_step(in_queue, out_queue):
        # 单步函数包装成循环执行
        while True:
            d = in_queue.get()
            r = func(d)
            out_queue.put(r)

    # 启动多进程/线程
    pool = Pool(workers, worker_step, (in_queue, out_queue))

    if callback is None:
        results = []

    # 后处理函数
    def process_out_queue():
        out_count = 0
        for _ in range(out_queue.qsize()):
            d = out_queue.get()
            out_count += 1
            if callback is None:
                results.append(d)
            else:
                callback(d)
        return out_count

    # 存入数据，取出结果
    in_count, out_count = 0, 0
    for d in iterable:
        in_count += 1
        while True:
            try:
                in_queue.put(d, block=False)
                break
            except queue.Full:
                out_count += process_out_queue()
        if in_count % max_queue_size == 0:
            out_count += process_out_queue()

    while out_count != in_count:
        out_count += process_out_queue()

    pool.terminate()

    if callback is None:
        return results


# 调用这个函数来多进程统计词频，大致代码如下：


def _batch_texts():
    texts = []
    for text in read_texts():
        texts.append(text)
        if len(texts) == 1000:
            yield texts
            texts = []
    if texts:
        yield texts


def _tokenize_and_count(texts):
    tokens = {}
    for text in texts:
        for token in tokenize(text):
            tokens[token] = tokens.get(token, 0) + 1
    return tokens


tokens = {}


def _total_count(result):
    for k, v in result.items():
        tokens[k] = tokens.get(k, 0) + v


# 10进程来完成词频统计
parallel_apply(
    func=_tokenize_and_count,
    iterable=_batch_texts(),
    workers=10,
    max_queue_size=200,
    callback=_total_count,
)

"""
整个流程是：
    _batch_texts将文本按批划分，每批为1000个文本；
    _tokenize_and_count用来对每一批样本进行统计；
    _total_count对每一批样本的结果进行汇总；
    最后parallel_apply用10进程实现这个过程。
"""
