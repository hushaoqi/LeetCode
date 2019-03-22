class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._data = []
        self._minData = []

    def push(self, x: int) -> None:
        """Add element x to the top of stack"""
        self._data.append(x)  # new item stored at end of list
        if len(self._minData) == 0:  # maintain the MinStack
            self._minData.append(x)
        else:
            if x < self._minData[-1]:
                self._minData.append(x)
            else:
                self._minData.append(self._minData[-1])

    def pop(self) -> None:
        """Remove and return the element from the top of the stack
        Raise Empty exception if the stack is empty
        """
        if len(self._data) == 0:
            raise Exception("Stack is empty")
        self._data.pop()  # remove last item from list
        self._minData.pop()

    def top(self) -> int:
        """Return (but not remove) the element at the top of the stack
        Raise Empty exception if the stack is empty
        """
        if len(self._data) == 0:
            raise Exception("Stack is empty")
        return self._data[-1]  # the last item in the list
    def getMin(self) -> int:
        if len(self._minData) == 0:
            raise Exception("Stack is empty")
        return self._minData[-1]
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
if __name__ == '__main__':
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.getMin())   #--> 返回 - 3.
    minStack.pop()
    print(minStack.top())      #--> 返回0.
    print(minStack.getMin())   #--> 返回 - 2.