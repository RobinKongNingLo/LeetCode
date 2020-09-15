class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        table = [0,0,0] + [0]*len(nums)
        for i in range(len(nums)):
            table[i+3] = max(table[i] + nums[i], table[i+1] + nums[i])
        return max(table)
            