class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        profit = 0

        for i in range(len(prices)):
            profit = max(profit,prices[i] - prices[l])
            if prices[i] < prices[l]:
                l = i
        return profit
            

            