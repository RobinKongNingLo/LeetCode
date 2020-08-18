class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set([])
        for i, num1 in enumerate(nums[:-2]):
            if i >= 1 and nums[i-1] == nums[i]: #Have seen this number before, pass
                continue
            seen = set([])
            for num2 in nums[i+1:]:
                n = - num2 - num1 #The answer we want
                if n in seen:
                    res.add((num1, n, num2))
                else:
                    seen.add(num2)
        return res
