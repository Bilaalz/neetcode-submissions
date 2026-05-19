class Solution:
    def maxArea(self, heights: List[int]) -> int:

        max_water = 0

        l = 0
        r = len(heights) - 1

        while l < r:
            width = r - l
            height = min(heights[l], heights[r])

            current = width * height

            if current > max_water:
                max_water = current
            
            if heights[l] < heights[r]:
                l += 1
            
            else:
                r -= 1
        
        return max_water

        