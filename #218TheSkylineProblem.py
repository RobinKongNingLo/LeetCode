class Solution(object):
    def getSkyline(self, buildings):
        heights = {0:1}
        maxheight = 0
        points = []
        res = []
        for building in buildings:
            tmp1 = [building[0], -building[2]]
            tmp2 = [building[1], building[2]]
            points.append(tmp1)
            points.append(tmp2)
        points.sort(key = lambda x: (x[0], x[1]))
        
        for point in points:
            if point[1] < 0:
                if -point[1] > maxheight:
                    res.append([point[0], -point[1]])
                    maxheight = -point[1]
                if -point[1] not in heights:
                    heights[-point[1]] = 1
                else:
                    heights[-point[1]] += 1
            else:
                heights[point[1]] -= 1
                if heights[point[1]] == 0:
                    del heights[point[1]]
                    if point[1] == maxheight:
                        maxheight = max(heights)
                        res.append([point[0], maxheight])
        
        return res