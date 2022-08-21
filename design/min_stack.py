# 155. Min Stack
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
# Implement the MinStack class:

# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.

class MinStack:

    def __init__(self):
        self.stack= []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val,val))
        else:
            self.stack.append((val,min(val,self.stack[-1][1])))

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]
        return None

    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]
        return None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()