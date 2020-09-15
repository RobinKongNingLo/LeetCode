class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tank = 0
        for i in range(len(gas)):
            j = i
            tank = 0
            while tank + gas[j] >= cost[j]:
                tank = tank + gas[j] - cost[j]
                j += 1
                if j >= len(gas):
                    j = 0
                if j == i:
                    return i
        return -1