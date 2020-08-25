class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        if target <= nums[left]:
            return left
        if target > nums[right]:
            return right + 1
        while right - left > 1:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid
            elif nums[mid] > target:
                right = mid
            else:
                return mid
        return right
