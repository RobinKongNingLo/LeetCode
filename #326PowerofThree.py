# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        dummy = ListNode(0)
        dummy.next = head
        evendummy = ListNode(0)
        evendummy.next = head.next
        odd = head
        even = head.next
        while True:
            if odd.next is None or even.next is None: #End condition (odd.next is None must be placed in front of even.next is None)
                odd.next = evendummy.next
                return dummy.next
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next