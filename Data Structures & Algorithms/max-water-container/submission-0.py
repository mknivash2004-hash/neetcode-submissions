class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_v = 0
        l = 0
        r = len(heights) - 1
        while l < r:
            vol = min(heights[l],heights[r]) * (r-l)
            max_v = max(vol,max_v)

            if(heights[l] < heights[r]):
                l += 1
            else:
                r -= 1
        return max_v