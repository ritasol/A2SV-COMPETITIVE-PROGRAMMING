class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        start = 0
        end = len(height) - 1
        
        while start < end:
            if height[start] < height[end]:
                area = max(area, height[start] * (end - start))
                start += 1
            else:
                area = max(area, height[end] * (end - start))
                end -= 1
        
        return area