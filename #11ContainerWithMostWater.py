class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1
        while left < right:
            h_left = height[left]
            h_right = height[right]
            area = min(h_left, h_right) * (right - left)
            max_area = max(max_area, area)
            if h_left < h_right:
                area = h_left * (right - left)
                left += 1
            else:
                area = h_right * (right - left)
                right -= 1
        
        return max_area