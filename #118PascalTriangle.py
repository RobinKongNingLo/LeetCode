class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if not numRows:
            return []
        out = [[1]]
        for m in range(1,numRows):
            nxtrow = [1] * (m+1)
            for n in range(1, len(nxtrow)-1):
                nxtrow[n] = currow[n-1] + currow[n]
            out.append(nxtrow)
            currow = nxtrow
        return out