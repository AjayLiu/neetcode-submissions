class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maxWater = 0
        while left < right:
            maxWater = max(maxWater, min(heights[left], heights[right]) * (right-left))
            if(heights[left] > heights[right]):
                right -= 1
            else:
                left += 1
            
        return maxWater