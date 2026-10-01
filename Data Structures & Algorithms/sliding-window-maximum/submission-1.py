class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
            res = []
            q = collections.deque()
            l , r = 0 , 0
                
            while r < len(nums): #while right still in bounds
                while q and nums[q[-1]] < nums[r]: #small ele less than curr
                    q.pop()
                q.append(r)

                #remove left val from window 
                if l > q[0]: #q[0] is left most val, out of window size
                    q.popleft()
                if (r + 1) >= k: #make sure window is atleast size K
                    res.append(nums[q[0]])
                    l+=1
                r +=1
            return res
