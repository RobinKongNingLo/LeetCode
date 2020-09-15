import heapq

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lowerhalf = []
        self.upperhalf = []

    def addNum(self, num: int) -> None:
        if len(self.lowerhalf) == 0: #Add first element to lowerhalf
            heapq.heappush(self.lowerhalf, -num)
            return
        
        if num <= -self.lowerhalf[0]:
            heapq.heappush(self.lowerhalf, -num)
        else:
            heapq.heappush(self.upperhalf, num)
        
        #Make sure that the difference between number of elements in lowerhalf and upperhalf is 0 or 1
        if len(self.lowerhalf) - len(self.upperhalf) == 2:
            heapq.heappush(self.upperhalf, -heapq.heappop(self.lowerhalf))
        elif len(self.upperhalf) - len(self.lowerhalf) == 2:
            heapq.heappush(self.lowerhalf, -heapq.heappop(self.upperhalf))

    def findMedian(self) -> float:
        if len(self.lowerhalf) == len(self.upperhalf): #The total number of elements is even
            return (-self.lowerhalf[0] + self.upperhalf[0]) / 2.0
        elif len(self.lowerhalf) > len(self.upperhalf):
            return -self.lowerhalf[0]
        else:
            return self.upperhalf[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()