class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._queueIn = []
        self._queueOut = []
    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self._queueIn.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if len(self._queueIn) == 0 and len(self._queueOut) == 0 :
            raise Exception("Stack is empty,pop failed")
        if len(self._queueOut) == 0:
            #if len(self._queueIn) > 1:
            self._queueOut.extend(self._queueIn[0:-1])
            temp = self._queueIn[-1]
            self._queueIn = []
            return temp
        if len(self._queueIn) == 0:
            #if len(self._queueOut) > 1:
            self._queueIn.extend(self._queueOut[0:-1])
            temp = self._queueOut[-1]
            self._queueOut = []
            return temp
        # if len(self._queueOut) != 0:
        #     return self._queueOut.pop()


    def top(self) -> int:
        """
        Get the top element.
        """
        if len(self._queueIn) == 0:
            return self._queueOut[-1]
        if len(self._queueOut) == 0:
            return self._queueIn[-1]
        if len(self._queueIn) == 0 and len(self._queueOut) == 0 :
            raise Exception("Stack is empty,top failed")
    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self._queueIn) == 0 and len(self._queueOut) == 0


class MyStack2(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.que1 = []
        self.que2 = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.que1.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if len(self.que1) < 2:
            return self.que1.pop(0)
        else:
            for i in range(len(self.que1) - 1):
                self.que2.append(self.que1.pop(0))
            result = self.que1.pop(0)
            while self.que2:
                self.que1.append(self.que2.pop(0))
            return result

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.que1[-1]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return not self.que1
# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
if __name__ == '__main__':
    myStack = MyStack()
    myStack.push(-2)
    myStack.push(0)
    myStack.push(-3)
    print(myStack.top())   #--> 返回 - 3.
    print(myStack.pop())   #--> 返回 - 3.
    print(myStack.top())      #--> 返回0.
    print(myStack.pop())  # --> 返回 0.
    print(myStack.pop())  # --> 返回 - 2.
    print(myStack.empty())   #--> 返回 True.
    print(myStack.pop())  # --> 返回 Error.