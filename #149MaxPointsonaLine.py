class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        out = 0
        for i in range(len(points)):
            dict = {'_':1}
            samepoints = 0
            x1, y1 = points[i][0], points[i][1]
            for j in range(i+1, len(points)):
                x2, y2 = points[j][0], points[j][1]
                if x1 == x2 and y1 == y2:
                    samepoints += 1
                    continue
                if x1 == x2:
                    slope = 'inf'
                else:
                    gcd = self.gcd(x1-x2, y1-y2)
                    slope = ((x1-x2)/gcd, (y1-y2)/gcd)
                if slope not in dict:
                    dict[slope] = 1
                dict[slope] = dict[slope] + 1
            out = max(out, max(dict.values()) + samepoints)
        return out
    
    def gcd(self, a, b):
        if b == 0:
            return a
        else:
            return self.gcd(b, a%b)
