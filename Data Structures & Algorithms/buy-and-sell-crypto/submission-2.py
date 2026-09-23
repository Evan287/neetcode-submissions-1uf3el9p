class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # if i > i -1 i - i-1 
        # add that difference to profit
        maxP = 0
        l, r = 0, 1
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        return maxP