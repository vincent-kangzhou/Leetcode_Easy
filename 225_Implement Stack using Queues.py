class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack=[]
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.stack.insert(0,x)


    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        top_=self.stack[0]
        self.stack=self.stack[1:]
        return top_
        

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.stack[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.stack)==0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
