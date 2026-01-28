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