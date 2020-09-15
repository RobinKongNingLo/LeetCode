class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        nodes = []
        node = head
        while node:
            nodes.append(node)
            node = node.next
        nodes = self.merge_sort(nodes)
        head = nodes[0]
        for i in range(len(nodes)-1):
            nodes[i].next = nodes[i + 1]
        nodes[-1].next = None
        
        return head
    
    def merge(self, list1, list2):
        len1 = len(list1)
        len2 = len(list2)
        idx1 = idx2 = 0
        sorted_list = []
        while idx1 < len1 and idx2 < len2:
            if list1[idx1].val <= list2[idx2].val:
                sorted_list.append(list1[idx1])
                idx1 += 1
            else:
                sorted_list.append(list2[idx2])
                print(list2[idx2].val)
                idx2 += 1
        if idx1 >= len1:
            sorted_list += list2[idx2:]
        else:
            sorted_list += list1[idx1:]
        return sorted_list
    
    def merge_sort(self, nodes):
        if len(nodes) <= 1:
            return nodes
        
        mid = len(nodes) // 2
        left = self.merge_sort(nodes[:mid])
        right = self.merge_sort(nodes[mid:])
        
        return self.merge(left, right)

#Better version, operating linked list directly
class Solution2:
    def sortList(self, head: ListNode) -> ListNode:
        #End condition
        if not head or not head.next:
            return head
        fast = head.next
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        #head2: head of the second half linked list
        head2 = slow.next
        #cut second half from first half 
        slow.next = None
        l = self.sortList(head)
        r = self.sortList(head2)
        return self.merge(l, r)
    
    def merge(self, l, r):
        if not l or not r:
            return l or r
        dummy = ListNode(0)
        node = dummy
        while l and r:
            if l.val <= r.val:
                node.next = l
                l = l.next
            else: 
                node.next = r
                r = r.next
            node = node.next
        if l:
            node.next = l
        elif r:
            node.next = r
            
        return dummy.next
