# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        l = res 
        carry = 0
        while l1 or l2 or carry:
            digit1 = l1.val if l1 else 0
            digit2 = l2.val if l2 else 0
            sum_ = digit1 + digit2 + carry
            digit = sum_ % 10
            carry = sum_ // 10
            l.next = ListNode(digit)
            l = l.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return res.next