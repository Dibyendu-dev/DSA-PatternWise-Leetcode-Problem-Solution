class MyStack:

    def __init__(self):
        self.main_q=deque()
        self.temp_q=deque()
        

    def push(self, x: int) -> None:
        self.temp_q.append(x)
        while self.main_q:
            self.temp_q.append(self.main_q.popleft())
        self.main_q,self.temp_q=self.temp_q,self.main_q
        

    def pop(self) -> int:
        return self.main_q.popleft()
        

    def top(self) -> int:
        return self.main_q[0]
        

    def empty(self) -> bool:
        return len(self.main_q) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()