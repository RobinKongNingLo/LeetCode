class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        table = {nums[0]:1}
        max_length = 1
        for i in range(1,len(nums)):
            max_tmp = 1
            for element in table:
                if nums[i] > element:
                    max_tmp = max(max_tmp, table[element] + 1)
            table[nums[i]] = max_tmp
            max_length = max(max_length, max_tmp)
        return max_length