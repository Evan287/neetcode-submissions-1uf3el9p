class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L, profit = 0, 0
        for R in range(1, len(prices)):
            while prices[L] > prices[R]:
                L += 1
            profit = max(profit, prices[R] - prices[L])
        return profit