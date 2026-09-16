class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l = 0
        r = len(heights) - 1

        volume = 0


        while l < r:
            width = r - l
            height = min(heights[l], heights[r])

            current_volume = width * height

            volume = max(current_volume, volume)

            if heights[l] < heights[r]:
                l += 1
            
            else:
                r -= 1
            
        return volume 