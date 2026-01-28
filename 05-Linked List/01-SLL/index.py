class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Traverse
def traverseList(head):
    curr=head
    while curr:
        curr= curr.next
    

def inserAtFirst(head,data):
    newnode = Node(data)
    newnode.next=head
    return newnode

def insertAtLast(head,data):
    newnode = Node(data)
    if head is None:
        return newnode
    
    curr = head
    while curr.next is not None:
        curr= curr.next

    curr.next = newnode
    return head

def insertAtAny(head,data,pos):
    newnode = Node(data)
    
    if pos < 1:
        return head
    
    if pos == 1:
        newnode.next=head
        return newnode
    
    curr = head
    for i in range(0,pos-1):
        if curr is None:
            return head
        curr=curr.next
    newnode.next = curr.next
    curr.next = newnode
    return head


def printSLL(head):
    curr = head
    while curr:
        print(curr.data,end=" -> ")
        curr= curr.next
    print(None)




if __name__ == "__main__":
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = Node(40)
    traverseList(head)
    printSLL(head)
    head = inserAtFirst(head,55)
    printSLL(head)
    head = insertAtLast(head,333)
    printSLL(head)
    head = insertAtAny(head,4548,2)
    printSLL(head)


