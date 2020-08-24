# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        i = 0
        dummy = ListNode(0)
        dummy.next = head
        fast = dummy
        slow = dummy
        while i <= n:
            fast = fast.next
            i += 1
        
        while fast:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next
        return dummy.next
