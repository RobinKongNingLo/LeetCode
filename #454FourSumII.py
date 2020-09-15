class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        cnt1 = collections.defaultdict(int)
        cnt2 = collections.defaultdict(int)
        res = 0
        for a in A:
            for b in B:
                cnt1[a+b] += 1
        for c in C:
            for d in D:
                cnt2[c+d] += 1
        for key in cnt1:
            if -key in cnt2:
                res += (cnt1[key] * cnt2[-key])
                
        return res
            