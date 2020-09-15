class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mult = 1
        zero_idx = []
        for i,num in enumerate(nums):
            if num == 0:
                if zero_idx:
                    return [0] * len(nums)
                zero_idx.append(i)
                continue
            mult *= num
        if zero_idx:
            nums = [0] * len(nums)
            nums[zero_idx[0]] = mult
            return nums
        for i in range(len(nums)):
            nums[i] = int(mult / nums[i])
        return nums