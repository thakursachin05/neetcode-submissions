# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        mHead = ListNode(0)
        curr = mHead
        head1 = list1
        head2 = list2

        while head1 and head2:
            if head1.val < head2.val:
                mHead.next = head1
                head1 = head1.next
            else:
                mHead.next = head2
                head2 = head2.next
            mHead = mHead.next
        
        if head1:
            mHead.next = head1
        if head2:
            mHead.next = head2
        
        return curr.next
        