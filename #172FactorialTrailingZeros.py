class Solution:
    def trailingZeroes(self, n: int) -> int:
        divider = 5
        ans = 0
        while divider <= n:
            ans += n//divider
            divider *= 5
        return ans