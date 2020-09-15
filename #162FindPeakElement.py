class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums = [-float("inf")] + nums + [-float("inf")]
        for i in range(1,len(nums)-1):
            if nums[i-1] < nums[i] and nums[i + 1] < nums[i]:
                return i-1
        return None