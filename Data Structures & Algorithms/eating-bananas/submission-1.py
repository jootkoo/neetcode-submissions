class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l , r = 1 , max(piles) #not using binary search to look through piles
        # but to narrow down options of what the solution can be
        result = r
        
        while l <= r:
            middle = (l + r) // 2
            totalH = 0
            for pile in piles:
                totalH += -(int(pile // -middle)) #take the ceiling 

            if totalH <= h: #if totalH less than H, it works, now find the smallest value
                result = min(result, middle)
                r = middle - 1
            else: #if the totalH too large, bannana rate needs to increase
                l = middle + 1
                
        return result

