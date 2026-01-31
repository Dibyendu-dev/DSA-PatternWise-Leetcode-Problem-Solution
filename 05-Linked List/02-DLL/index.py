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

def printdll(head):
    temp = head
    while temp:
        print(temp.data,end="<->")
        temp= temp.next
    print()


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
