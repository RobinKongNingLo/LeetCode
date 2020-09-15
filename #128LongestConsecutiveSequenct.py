class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        consecutive = 1
        maxConsecutive = 1
        for i in range(len(nums)-1):
            if nums[i] + 1 == nums[i+1]:
                consecutive += 1
            elif nums[i] == nums[i+1]:
                continue
            else:
                maxConsecutive = max(consecutive, maxConsecutive)
                consecutive = 1
        maxConsecutive = max(consecutive, maxConsecutive)
        return maxConsecutive
            