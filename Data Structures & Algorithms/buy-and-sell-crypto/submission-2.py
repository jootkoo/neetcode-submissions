class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #sliding window
        mProfit = 0
        l , r = 0 , 1 #both pointers move in same direction

        while r < len(prices):
            if prices[l] < prices[r]: #sellable stock
                mProfit = max(mProfit, prices[r] - prices[l])
            else: #otherwise move left pointer up, 
                l = r
            r += 1 #keep moving right pointer down 
        return mProfit

            