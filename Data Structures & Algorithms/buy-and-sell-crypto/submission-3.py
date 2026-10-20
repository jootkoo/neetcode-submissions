class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = prices[0] #left pointer
        highest = 0
        for x in prices:
            highest = max(highest, x - l)
            if x < l:
                l = x
        return highest
                

            