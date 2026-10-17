# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minHeap = []

        for i, l1 in enumerate(lists):
            if l1:
                heapq.heappush(minHeap, (l1.val, i, l1))
        
        res = dummy = ListNode(0)
        counter = len(lists)
        
        while minHeap:
            val, i, node = heapq.heappop(minHeap)
            dummy.next = node
            dummy = dummy.next
            if node.next:
                counter += 1
                heapq.heappush(minHeap, (node.next.val, counter, node.next))
        
        return res.next
        