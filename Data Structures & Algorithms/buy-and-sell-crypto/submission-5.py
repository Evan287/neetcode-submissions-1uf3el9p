class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L, profit = 0, 0
        for R in range(1, len(prices)):
            if prices[L] > prices[R]:
                L = R
            profit = max(profit, prices[R] - prices[L])
        return profit