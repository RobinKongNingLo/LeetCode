class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        FoundTarget = False
        low = 0
        high = len(nums) - 1
        point = int
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                point = mid
                FoundTarget = True
                break
            if nums[mid] > target:
                high = mid -1
            else:
                low = mid + 1
        
        if not FoundTarget:
            return [-1, -1]
        
        first = last = point
        while True:
            if first > 0 and nums[first - 1] == nums[first]:
                first = first - 1
            else: break
                    
        while True:
            if last < len(nums)-1 and nums[last + 1] == nums[last]:
                last = last + 1
            else: break
                    
        return [first, last]