class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        nsort = sorted(nums)
        nsort = [n for i,n in enumerate(nsort) if i == 0 or nsort[i-1] != n]
        tree = [0] * (len(nsort) + 1)
        res = [0] * len(nums)
        for k,n in enumerate(reversed(nums)):
            i = bisect.bisect_left(nsort, n)
            tree[i+1] += 1
            res[len(nums) - k - 1] = sum(tree[:i+1])
        return res