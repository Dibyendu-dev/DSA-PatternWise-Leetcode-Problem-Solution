class Node:
    def __init__(self,data):
        self.data =data
        self.next=None

class LinkedListCircularQueue:
    def __init__(self,capacity=5):
        self.capacity=capacity
        self._front=None
        self._rear=None
        self._size=0

    def is_empty(self):
        return self._size == 0
    
    def is_full(self):
        return self._size == self.capacity
    
    def size(self):
        return self._size
    
    def enqueue(self,val):
        if self.is_full():
            raise Exception("Queue is Full")
        new_node = Node(val)
        if self.is_empty():
            self._front=self._rear=new_node
            new_node.next=new_node
        else:
            self._rear.next=new_node
            self._rear=new_node
            self._rear.next=self._front   
        self._size +=1

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is Empty")
        removed_value = self._front.data
        if self._size == 1:
            self._front=None
            self._rear=None
        else:
            self._front=self._front.next
            self._rear.next=self._front
        self._size -=1
        return removed_value

    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        curr=self._front
        elements=[]
        for _ in range(self._size):
            elements.append(str(curr.data))
            curr = curr.next
        print("Queue (front to rear):", " <- ".join(elements))


if __name__ == "__main__":
    q= LinkedListCircularQueue()
    q.enqueue(27)
    q.enqueue(17)
    q.enqueue(7)
    q.enqueue(37)

    q.display()

    q.dequeue()
    q.display()


    q.enqueue(57)
    q.display()

    q.enqueue(77)
    q.display()
    q.dequeue()
    q.enqueue(87)
    q.display()
    

    

