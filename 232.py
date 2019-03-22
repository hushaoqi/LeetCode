class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._stackPush = []
        self._stackPop = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self._stackPush.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if len(self._stackPush) == 0:
            raise Exception("The queue is empty,pop failed")
        # 弹出stackPush栈中除栈底外的所有元素，放入stackPop栈中
        for i in range(len(self._stackPush)-1):
            self._stackPop.append(self._stackPush.pop())
        # 弹出并取得stackPush栈底元素，即队首元素
        temp = self._stackPush.pop()
        # 恢复 stackPush栈，即恢复队
        for j in range(len(self._stackPop)):
            self._stackPush.append(self._stackPop.pop())
        return temp

    def peek(self) -> int:
        """
        Get the front element.
        """
        if len(self._stackPush) != 0:
            return self._stackPush[0]
        else:
            raise Exception("The queue is empty,peek failed")

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self._stackPush) == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
if __name__ == '__main__':
    myqueue = MyQueue()
    myqueue.push(1)
    myqueue.push(2)
    print(myqueue.pop())
    myqueue.push(3)
    myqueue.push(4)
    print(myqueue.pop())
    print(myqueue.peek())
