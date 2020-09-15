class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s = set([])
        for i in range(len(nums)):
            if nums[i] in s:
                s.remove(nums[i])
            else:
                s.add(nums[i])
        return min(s)