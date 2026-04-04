# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        temp = head
        length =1

        while temp.next:
            length += 1
            temp = temp.next

        temp.next = head
        k = k % length

        end = length - k
        while end > 0:
            temp = temp.next
            end -=1

        head = temp.next
        temp.next = None

        return head 