class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        while nums:
            a = nums.pop()
            length = len(nums)
            for i in range(length):
                if nums[i] == target - a:
                    return [i, length]



    