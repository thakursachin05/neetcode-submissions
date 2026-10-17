# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = dummy = ListNode(0)
        carry = 0
        while l1 and l2:
            digit = l1.val + l2.val + carry
            carry = digit//10
            dummy.next = ListNode(digit%10)
            dummy = dummy.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            digit = l1.val + carry
            carry = digit//10
            dummy.next = ListNode(digit%10)
            dummy = dummy.next
            l1 = l1.next
        
        while l2:
            digit = l2.val + carry
            carry = digit//10
            dummy.next = ListNode(digit%10)
            dummy = dummy.next
            l2 = l2.next
        
        if carry:
            dummy.next = ListNode(carry)

        return res.next