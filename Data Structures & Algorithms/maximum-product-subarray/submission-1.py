class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        Max = max(nums)
        curMin,curMax = 1,1
        for n in nums:
            tmp = curMax*n
            curMax = max(tmp,curMin*n,n)
            curMin = min(tmp,curMin*n,n)
            Max = max(Max,curMax)
        return Max