class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        
        intervals = sorted(intervals)
        out = [intervals[0]]
        for interval in intervals[1:len(intervals)+1]:
            if interval[0] <= out[-1][1]:
                out[-1] = [out[-1][0], max(interval[1], out[-1][1])]
            else:
                out.append(interval)
        
        return out