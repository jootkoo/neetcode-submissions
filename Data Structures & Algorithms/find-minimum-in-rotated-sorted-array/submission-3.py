class Solution:
    def findMin(self, nums: List[int]) -> int:
        l , r = 0 , len(nums) - 1 #start and end of array
        middle = (l + r) // 2
        smallest = nums[0] #set default 
        #if true this means that that side is sorted already, either the middle is the least
        #or the min value is behind it...
        if nums[middle] < nums[r]:
            while middle >= l: #iterate backwards towards L
                smallest = min(smallest, nums[middle])
                middle -= 1
        else:
            while middle <= r:
                smallest = min(smallest, nums[middle])
                middle += 1
        return smallest