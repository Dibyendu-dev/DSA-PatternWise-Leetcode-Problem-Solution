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

def delFirst(head):
    if head is None:
        return None
    temp=head
    head= head.next
    temp=None
    return head

def delLast(head):
    if head is None:
        return None
    if head.next is None:
        return None
    
    secLast = head
    while secLast.next.next is not None:
        secLast = secLast.next
    secLast.next=None
    return head

def delAtAny(head,position):
    if head is None or position < 1:
        return head
    
    temp = head
    
    if position == 1:
        head = temp.next
        return head
    
    for i in range(1,position-1):
        if temp.next is None:
            return head
        temp = temp.next

    if temp.next is None:
        return head
    temp.next = temp.next.next
    return head

def search(head,val):
    curr = head
    while curr is not None:
        if curr.data == val:
            return True
        curr = curr.next
    return False

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
    head= delFirst(head)
    printSLL(head)
    head= delLast(head)
    printSLL(head)
    head= delAtAny(head,2)
    printSLL(head)

    if search(head,50):
        print("search value is found")
    else:
        print("search value is not found")
        






