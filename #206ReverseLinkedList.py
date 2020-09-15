class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        ListNodes = []
        node = head
        while node:
            ListNodes.append(node)
            node = node.next
        dummy = ListNode(0)
        i = 1
        node = dummy
        while i <= len(ListNodes):
            node.next = ListNodes[-i]
            i = i+1
            node = node.next
        node.next = None
        return dummy.next