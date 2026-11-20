class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p = 0
        buy = prices[0]
        for i in range(1,len(prices)):
            buy = min(buy,prices[i])
            max_p = max(max_p,prices[i]-buy)
        return max_p
