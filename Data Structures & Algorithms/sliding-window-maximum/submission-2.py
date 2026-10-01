class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
            res = []
            q = collections.deque()
            l , r = 0 , 0
                
            while r < len(nums): #while right still in bounds
                while q and nums[q[-1]] < nums[r]: 
                    #if the last element in the queue is less than the curr, remove it
                    #otherwise the smaller num will be appeneded behind it
                    q.pop() 
                q.append(r) #stores the INDEX

                #remove left val from window 
                if l > q[0]: #checks if the index of the greatest ele is not in range
                    q.popleft()
                if (r + 1) >= k: #make sure window is atleast size K
                    res.append(nums[q[0]]) #append largest 
                    l+=1
                r +=1
            return res
