class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        winmax = max(nums[:k])
        res = [winmax]
        i = 1
        while i+k <= len(nums):
            if nums[i-1] == winmax:
                winmax = max(nums[i:i+k])
            elif nums[i+k-1] > winmax:
                winmax = nums[i+k-1]
            res.append(winmax)
            i += 1
        return res