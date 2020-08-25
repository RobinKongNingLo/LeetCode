class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        left = 0
        right = len(nums) - 1
        if target < nums[left] or target > nums[right]:
            return [-1, -1]
        
        #Step1: find the target
        
        targetidx = -1
        while right >= left:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                targetidx = mid
                break
        
        #If target is not in nums
        if targetidx == -1:
            return [-1, -1]
        
        #Step2: find the start and the end
        start = end = targetidx
        
        while True:
            if start-1 >=0 and nums[start-1] == target:
                start -= 1
            else:
                break
        
        while True:
            if end+1 <= right and nums[end+1] == target:
                end += 1
            else:
                break
        
        return [start, end]
