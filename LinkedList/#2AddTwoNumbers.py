# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = ListNode(0)
        dummy = l3
        carry = 0
        while l1 or l2 or carry:
            l1val = l1.val if l1 else 0
            l2val = l2.val if l2 else 0
            tmp = l1val + l2val + carry
            if tmp >= 10:
                l3.next = ListNode(tmp-10)
                carry = 1
            else:
                l3.next = ListNode(tmp)
                carry = 0
            l3 = l3.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return dummy.next
            
