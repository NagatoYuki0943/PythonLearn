

class Node:
    # 这里的 prev 的类型是自己,但是需要加引号,编程string,否则会无法通过检查,因为 Node 还没有被定义
    # 事实上所有的 type hint 都可以放入引号中
    def __init__(self, prev: "Node") -> None:
        """
        Initializes a new instance of the Node class.
        Args:
            prev (Node): The previous node in the linked list.
        Returns:
            None
        """
        self.prev = prev
        self.next = None
