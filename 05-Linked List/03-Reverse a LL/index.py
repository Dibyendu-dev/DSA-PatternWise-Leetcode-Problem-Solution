class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def printSLL(head):
    curr = head
    while curr:
        print(curr.data,end=" -> ")
        curr= curr.next
    print(None)

def reverseLL(head):
    curr = head
    prev = None

    while curr is not None:
        nextnode = curr.next
        curr.next = prev
        prev = curr
        curr = nextnode
    return prev

if __name__ == "__main__":
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = Node(40)
    printSLL(head)
    head=reverseLL(head)
    printSLL(head)