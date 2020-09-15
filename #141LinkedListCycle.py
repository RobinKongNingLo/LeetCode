class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        s = set([])
        node = head
        while node:
            if node in s:
                return True
            else:
                s.add(node)
            node = node.next
        return False
        
    