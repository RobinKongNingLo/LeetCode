# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        #End case 1
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        mid = len(lists) // 2
        l = self.mergeKLists(lists[:mid])
        r = self.mergeKLists(lists[mid:])
        return self.mergeTwoLists(l, r)
    
    def mergeTwoLists(self, l1, l2):
        #Dummy value first
        l3 = ListNode(0)
        dummy = l3
        while l1 and l2:
            if l1.val < l2.val:
                l3.next = ListNode(l1.val)
                l1 = l1.next
            else:
                l3.next = ListNode(l2.val)
                l2 = l2.next
            l3 = l3.next    
        if l1:
            l3.next = l1
        if l2:
            l3.next = l2
        
        return dummy.next