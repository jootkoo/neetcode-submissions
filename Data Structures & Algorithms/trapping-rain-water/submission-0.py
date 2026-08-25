class Solution:
    def trap(self, height: List[int]) -> int:
        maxL = []
        maxR = []
        maxSeen = 0
        sums = 0
        for i in range(len(height)): #maxL array
            maxSeen = max(maxSeen, height[i])
            maxL.append(maxSeen)
        maxSeen = 0
        for i in range(len(height)-1, -1, -1 ): #maxL array
            maxSeen = max(maxSeen, height[i])
            maxR.append(maxSeen)
        maxR.reverse()
        for i in range(len(height)):
            if (min(maxL[i], maxR[i]) - height[i]) > 0:
                sums += min(maxL[i], maxR[i]) - height[i]

        return sums




