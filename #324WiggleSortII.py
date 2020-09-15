class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        numsorted = [] + nums
        numsorted.sort()
        left = ceil(len(numsorted) / 2) - 1
        right = len(nums) - 1
        i = 0
        j = 1
        while j < len(nums):
            nums[i] = numsorted[left]
            nums[j] = numsorted[right]
            left -= 1
            right -= 1
            i += 2
            j += 2
        if i < len(nums):
            nums[i] = numsorted[left]