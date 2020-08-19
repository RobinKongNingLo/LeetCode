from collections import defaultdict
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        seen = defaultdict(list)
        res = set()
        for i in range(len(nums)):
            for j in range(i):
                current = nums[i] + nums[j]
                n = target - current
                if n in seen:
                    for a, b in seen[n]:
                        if len({i, j, a, b}) == 4:
                            res.add(tuple(sorted([nums[i], nums[j], nums[a], nums[b]])))
                seen[current].append((i,j))
        return res
