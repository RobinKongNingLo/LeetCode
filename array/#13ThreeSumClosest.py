class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        mindist = float('inf')
        for i, num1 in enumerate(nums):
            if i >= 1 and nums[i-1] == nums[i]:
                continue
            l = i+1 #left pointer
            r = len(nums) - 1
            while l < r:
                dist = num1 + nums[l] + nums[r] - target #Object: distance is the closest to 0
                if dist == 0:
                    return target
                if abs(dist) < abs(mindist):
                    mindist = dist
                if dist < 0: #Then dist needs to become bigger, l move right
                    l = l+1
                else: #The dist needs to become smaller, r move left
                    r = r-1
        return mindist + target
