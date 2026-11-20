class Solution:
    def climbStairs(self, n: int) -> int:
        arr = [1,1]
        for i in range(n-1):
            arr[-1],arr[-2] = arr[-1] + arr[-2], arr[-1]
        return arr[-1]
