class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        minprice = min(prices)
        maxprice = max(prices)
        minidx = prices.index(minprice)
        maxidx = prices.index(maxprice)
        if maxidx > minidx:
            return maxprice - minprice
        if maxidx == minidx:
            return 0
        leftmax = self.maxProfit(prices[:maxidx+1])
        midmax = self.maxProfit(prices[maxidx+1:minidx])
        rightmax = self.maxProfit(prices[minidx:])
        return max(leftmax, midmax, rightmax)