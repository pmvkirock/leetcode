# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head == None:
            return False
        slow, head = head, head.next
        while head != slow:
            if head == None or head.next == None:
                return False
            head, slow = head.next.next, slow.next
            
        return True