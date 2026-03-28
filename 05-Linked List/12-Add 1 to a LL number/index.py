class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addOne(self, head):
        if not head:
            return ListNode(1)
        head = self.reverse(head)
        carry = 1
        current = head
        while current is not None and carry:
            sum = current.val + carry
            current.val = sum % 10 
            carry = sum // 10
            if current.next is None and carry:
                current.next = ListNode(0)  
            current = current.next
        return self.reverse(head)
            
    
    def reverse(self, head):
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev