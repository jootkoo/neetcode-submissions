class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0 , len(nums) - 1
        smallest = nums[0]
        middle = (l + r) // 2
        smallest = min(smallest, nums[middle])


        if nums[middle] < nums[r]: #if this is true that means that its already sorted
            while middle > l: #meaning the smaller value may be behind
                middle -= 1
                smallest = min(smallest, nums[middle])
        else:
            while middle < r:
                middle += 1
                smallest = min(smallest, nums[middle])
                
        
        return smallest
        
                

                
            

        



