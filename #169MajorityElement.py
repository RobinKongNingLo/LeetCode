class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dict = {}
        m = len(nums) / 2
        for num in nums:
            if num in dict:
                dict[num] += 1
                if dict[num] >m:
                    return num
            else:
                dict[num] = 1