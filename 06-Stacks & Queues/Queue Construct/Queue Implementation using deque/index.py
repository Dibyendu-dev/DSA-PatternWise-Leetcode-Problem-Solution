from collections import deque

class Deque:
    def __init__(self):
        self._dq = deque()

    def is_empty(self):
        return len(self._dq) == 0
    
    def enqueue(self,data):
        self._dq.append(data)
        print(f"enqueue: {data}")

    def dequeue(self):
        if self.is_empty():
            print(f"queue is empty")
            return None
        data = self._dq.popleft()
        print(f"dequeue: {data}")
        return data
    
    def __str__(self):
        if self.is_empty():
            return "queue: []"
        return (" | ").join([str(x) for x in self._dq])
    
    def __repr__(self):
        return (" | ").join([str(x) for x in self._dq])
        

if __name__ == "__main__":
    dq = Deque()
    dq.enqueue(10)
    dq.enqueue(20)
    dq.enqueue(30)
    dq.enqueue(40)
    dq.enqueue(50)
    print(dq)
    dq.dequeue()
    print(dq)