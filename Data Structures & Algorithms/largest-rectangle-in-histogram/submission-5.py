class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_a = 0
        stack = [] #(i,h)
        for i,h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                ind, hei = stack.pop()
                max_a = max(max_a,(i-ind)*hei)
                start = ind
            stack.append((start,h))

        for i,h in stack:
            max_a = max(max_a,h*(len(heights)-i))
        return max_a