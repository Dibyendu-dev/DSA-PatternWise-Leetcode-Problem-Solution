class CircularQueue:
    def __init__(self,capacity=5):
        self.capacity = capacity
        self._data = [None] * self.capacity
        self._size=0
        self._front=0
        self._rear=0

    def is_full(self):
        return self._size == self.capacity
    
    def is_empty(self):
        return self._size == 0
    
    def enqueue(self,val):
        if self.is_full():
            print(f"queue is full")
            return None
        self._data[self._rear] = val
        self._rear = (self._rear + 1) % self.capacity
        self._size = self._size + 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        else:
            val = self._data[self._front]
            self._data[self._front]= None
            self._front=(self._front+1) % self.capacity
            self._size=self._size-1
            return val
        
    def __str__(self):
        return str(self._data)
    
    def __repr__(self):
        return str(self._data)
        
if __name__ == "__main__":
    q = CircularQueue()
    q.enqueue(27)
    q.enqueue(17)
    q.enqueue(7)
    q.enqueue(37)

    print(q)

    q.dequeue()
    print(q)
    q.enqueue(71)
    q.enqueue(34)
    print(q)