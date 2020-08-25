class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dict[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dict or timestamp < self.dict[key][0][1]:
            return ""
        timestamps = self.dict[key]
        left = 0
        right = len(timestamps) - 1
        while left <= right:
            mid = (left + right) // 2
            if timestamp >= timestamps[mid][1]:
                left = mid + 1
            else:
                right = mid - 1
        return self.dict[key][right][0]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
