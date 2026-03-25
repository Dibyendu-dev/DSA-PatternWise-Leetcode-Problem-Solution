# Definition of singly linked list:
from multiprocessing import dummy


class ListNode:
    def __init__(self, x=0, next=None):
        self.data = x
        self.next = next

class Solution:
    def addTwoNumbers(self, linkedList1, linkedList2):
        dummy = ListNode()
        temp = dummy
        carry = 0

        while linkedList1 or linkedList2 or carry:
            sum = 0

            if linkedList1:
                sum += linkedList1.data
                linkedList1 = linkedList1.next

            if linkedList2:
                sum += linkedList2.data
                linkedList2 = linkedList2.next
            
            sum += carry
            carry = sum // 10

            node = ListNode(sum % 10)
            temp.next = node
            temp = temp.next
        
        return dummy.next