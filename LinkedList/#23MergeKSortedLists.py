# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        
        mid = len(lists) // 2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])
        
        return self.mergeTwoLists(left, right)
    
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        l3 = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                l3.next = ListNode(l1.val)
                l1 = l1.next
            else:
                l3.next = ListNode(l2.val)
                l2 = l2.next
            l3 = l3.next
            
        if l1:
            l3.next = l1
        elif l2:
            l3.next = l2
            
        return dummy.next
