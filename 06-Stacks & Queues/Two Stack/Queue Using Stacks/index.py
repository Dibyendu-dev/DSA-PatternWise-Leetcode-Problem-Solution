class MyQueue:

    def __init__(self):
        self.main_stack=[]
        self.temp_stack=[]
        

    def push(self, x: int) -> None:
        self.main_stack.append(x)

    def pop(self) -> int:
        if not self.temp_stack:
            while self.main_stack:
                self.temp_stack.append(self.main_stack.pop())
        return self.temp_stack.pop()
        

    def peek(self) -> int:
        if not self.temp_stack:
            while self.main_stack:
                self.temp_stack.append(self.main_stack.pop())
        return self.temp_stack[-1]
        

    def empty(self) -> bool:
        if self.main_stack or self.temp_stack:
            return False
        return True
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()