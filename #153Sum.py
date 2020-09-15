class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sol = set()
        for i in range(len(nums) - 2):
            num = nums[i]
            if i >= 1 and num == nums[i-1]:
                continue
            l = i+1
            r = len(nums) - 1
            while r > l:
                if nums[l] + nums[r] + num > 0:
                    r-= 1
                elif nums[l] + nums[r] + num < 0:
                    l += 1
                else:
                    sol.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
        return list(sol)

#Faster solution:
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        for i,num1 in enumerate(nums[:-2]):
            if i >= 1 and num1 == nums[i-1]:
                continue
            h = {}
            for num in nums[i+1:]:
                n = - num1 - num
                if n not in h:
                    h[num] = 1
                else:
                    res.add((num1, num, n))
        return list(res)