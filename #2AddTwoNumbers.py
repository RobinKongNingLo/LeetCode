class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def ListToListNode(numbers):

    # Convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        "Initialize result link list"
        result = ListNode(0)
        result_tail = result
        carry = 0
        
        "Start the adding process, while loop ends when l1 and l2 are none, carry is 0"
        while(l1 or l2 or carry):
            l1val = (l1.val if l1 else 0)
            l2val = (l2.val if l2 else 0)
            [carry, res] = divmod(l1val + l2val + carry, 10)
            result_tail.next = ListNode(res)
            result_tail = result_tail.next
            
            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)
        
        return result.next
