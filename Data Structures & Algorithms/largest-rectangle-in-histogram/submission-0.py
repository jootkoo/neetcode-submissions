class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # index, height
        area = 0
        for i,n in enumerate(heights):
            start = i
            while stack and stack[-1][1] > n:
                recentI, recentH = stack.pop()
                area = max(area , recentH * (i - recentI))
                start = recentI #set the most recently popped index to start 
            stack.append([start, n])
            #set the index to start because it can still become a rectangle

        for i, h in stack: #picks up the everything else left in the stack 
        #this is the remaining end, no shorter bards appeared after therefore...
            area = max(area, h * (len(heights)- i))
        return area
