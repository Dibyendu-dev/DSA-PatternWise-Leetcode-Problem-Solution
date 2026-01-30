class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

   
    @staticmethod
    def detectLoop(head):
        slow = head
        fast = head

        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
            
        return False

if __name__ == "__main__":
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = head.next

    if Node.detectLoop(head):
        print("true")
    else:
        print("false")

   