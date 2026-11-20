class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_a = 0
        stack = [] # pair : (ind,height)

        for i,h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                si,sh = stack.pop()
                max_a = max(max_a,sh*(i-si))
                start = si
            stack.append((start,h))
        
        for i,h in stack:
            max_a = max(max_a,(len(heights)-i)*h)
        return max_a