class Solution:
    def trap(self, height: List[int]) -> int:
        sums = 0
        l = 0
        r = len(height) - 1
        maxL = 0
        maxR = 0
        while l < r:
            maxR = max(maxR, height[r])
            maxL = max(maxL, height[l])
            if maxR < maxL:
                r -= 1 #move pointer
                if min(maxR, maxL) - height[r] > 0:
                    sums += min(maxR, maxL) - height[r]
            else:
                l += 1
                if min(maxR, maxL) - height[l] > 0:
                    sums += min(maxR, maxL) - height[l]



        return sums




