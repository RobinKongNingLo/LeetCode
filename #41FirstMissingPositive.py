class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        j = 1
        
        while True:
            if j not in nums:
                return j 
            j+=1