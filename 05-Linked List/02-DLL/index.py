class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

def fwd_traverse(head):
    temp = head
    while temp is not None:
        print(temp.data,end= " ")
        temp=temp.next
    print()   

def bck_traverse(head):
    temp = head
    while temp is not None:
        print(temp.data,end= " ")
        temp=temp.prev
    print() 

def inserAtFront(head,data):
    newNode = Node(data)
    newNode.next = head
    if head is not None:
        head.prev = newNode
    head = newNode
    return head

def inserAtEnd(head,data):
    newNode = Node(data)
    if head is None:
        return newNode
    temp = head
    while temp.next is not None:
        temp = temp.next
    temp.next = newNode
    newNode.prev = temp
    return head

def inserAtPos(head, pos, data):
    if pos < 1:
        return head
    if pos == 1:
        return inserAtFront(head, data)
    
    newNode = Node(data)
    temp = head
    for _ in range(pos - 1):
        if temp is None:
            return head
        temp = temp.next
    if temp is None:
        return head
    newNode.next = temp.next
    newNode.prev = temp
    if temp.next is not None:
        temp.next.prev = newNode
    temp.next = newNode
    return head

def printdll(head):
    temp = head
    while temp:
        print(temp.data,end="<->")
        temp= temp.next
    print(None)


if __name__=="__main__":
    head = Node(10)

    head.next = Node(20)
    head.next.prev = head

    head.next.next = Node(30)
    head.next.next.prev = head.next

    head.next.next.next = Node(40)
    head.next.next.next.prev = head.next.next

    fwd_traverse(head)
    bck_traverse(head.next.next.next)

    printdll(head)
