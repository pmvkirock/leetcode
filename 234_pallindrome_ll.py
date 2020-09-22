# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        num1, num2, count = 0, 0, 1
        while head != None: 
            num1 = num1*10 + head.val
            num2 = head.val*count + num2
            count = count*10
            head=head.next
        
        return num1 == num2
        
        
        