# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        slowest = dummy
        while True:
            slow = slowest.next
            if not slow:
                return dummy.next
            fast = slow.next
            if not fast:
                return dummy.next
            #slow and fast both exist
            slow.next = fast.next
            fast.next = slow
            slowest.next = fast
            slowest = slowest.next.next
