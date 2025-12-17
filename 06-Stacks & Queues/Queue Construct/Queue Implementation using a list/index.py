class Queue:
    def __init__(self,capacity=5):
        self.capacity = capacity
        self._data = [None] * self.capacity
        self._size=0
        self._front=0
        self._rear=0

    def eneque(self,value):
        if self._rear == self.capacity:
            raise IndexError("Queue is full")
        else:
            self._data[self._rear]=value
            self._rear=self._rear+1
            self._size=self._size+1

    def deque(self):
        if self._size==0:
            raise IndexError("Queue is empty")
        else:
            val = self._data[self._front]
            self._data[self._front]= None
            self._front=self._front+1
            self._size=self._size=1
            return val

    def __str__(self):
        return str(self._data)
    
    def __repr__(self):
        return str(self._data)
    
    def _is_empty(self):
        return self._size==0
    
    def _is_Full(self):
        return self._rear == self.capacity
    
    def front(self):
        return self._data[self._front]
    

q = Queue()
q.eneque(27)
q.eneque(17)
q.eneque(7)
q.eneque(37)

print(q)

q.deque()
print(q)

q.eneque(57)
print(q)

print(q.front())
# q.eneque(67)
# print(q)