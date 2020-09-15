from collections import deque
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.dequeue = deque()
        self.flatten(nestedList)
    
    def flatten(self, nestedList):
        for element in nestedList:
            if element.isInteger():
                self.dequeue.append(element.getInteger())
            else:
                self.flatten(element.getList())
            
    def next(self) -> int:
        return self.dequeue.popleft()
    
    def hasNext(self) -> bool:
         return self.dequeue
            