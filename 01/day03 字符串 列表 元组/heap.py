# Python的heapq模块实现了堆队列算法，通常用于创建优先队列。它基于最小堆结构，这意味着每次弹出堆时，返回的是最小的元素。

import heapq


# 创建堆
# 使用heapq.heapify()函数将一个列表转换为堆。
data = [5, 1, 3, 7, 4]
heapq.heapify(data)
print(data)  # [1, 4, 3, 7, 5]

# 插入元素
# 使用heapq.heappush(heap, item)将元素插入堆中，并保持堆的属性。
heapq.heappush(data, 2)
print(data)  # [1, 4, 2, 7, 5, 3]

# 弹出最小元素
# 使用heapq.heappop(heap)从堆中弹出并返回最小元素，同时保持堆的结构。
smallest = heapq.heappop(data)
print(smallest)  # 1
print(data)      # [2, 4, 3, 7, 5]

# 同时插入和弹出
# heapq.heappushpop(heap, item)先将元素插入堆中，然后弹出并返回最小元素。
result = heapq.heappushpop(data, 6)
print(result)  # 2
print(data)    # [3, 4, 6, 7, 5]

# 替换最小元素
# heapq.heapreplace(heap, item)弹出最小元素并将新元素插入堆中。
result = heapq.heapreplace(data, 0)
print(result)  # 3
print(data)    # [0, 4, 6, 7, 5]

# 获取n个最大或最小元素
largest = heapq.nlargest(3, data)
smallest = heapq.nsmallest(1, data)
print(largest)   # [7, 6, 5]
print(smallest)  # [0]
print(data)      # [0, 4, 6, 7, 5]


# 优先队列示例
# 可以使用heapq模块实现优先队列。优先队列中的每个元素通常是一个元组，其中第一个值表示优先级，第二个值是实际数据。
class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

# 使用示例
pq = PriorityQueue()
pq.push('task1', priority=2)
pq.push('task2', priority=1)
pq.push('task3', priority=3)

print(pq.pop())  # 'task2'
print(pq.pop())  # 'task1'
