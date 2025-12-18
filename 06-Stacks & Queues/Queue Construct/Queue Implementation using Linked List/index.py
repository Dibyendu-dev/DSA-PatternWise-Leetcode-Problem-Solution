class Node:
    def __init__(self,data):
        self.data =data
        self.next=None

class LinkedListQueue:
    def __init__(self):
        self._front=None
        self._rear=None
        self._size=0

    def is_empty(self):
        return self._front is None

    def enqueue(self,val):
        new_node = Node(val)
        if self._rear is None:
            self._front=new_node
            self._rear=new_node
        else:
            self._rear.next=new_node
            self._rear=new_node

        self._size +=1

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        val=self._front.data
        self._front=self._front.next

        if self._front is None:
            self._rear=None
        
        self._size -=1
        return val
    
    def is_peek(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        return self._front.data
    
    def size(self):
        return self.size
    
    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        curr=self._front
        elements=[]
        while curr:
            elements.append(str(curr.data))
            curr= curr.next
        print("Queue (front to rear):", " <- ".join(elements))
    

q= LinkedListQueue()
q.enqueue(27)
q.enqueue(17)
q.enqueue(7)
q.enqueue(37)

q.display()

q.dequeue()
q.display()


q.enqueue(57)
q.display()

    