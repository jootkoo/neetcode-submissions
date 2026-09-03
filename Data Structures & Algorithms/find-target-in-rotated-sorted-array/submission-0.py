class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        middle = (l + r) // 2

        while l <= r: # to find a value that is smaller , move left
            middle = (l + r) // 2

            if nums[middle] == target:
                return middle

            if nums[l] <= nums[middle]: #this means that the left side is sorted
                #if the target is less than the middle and greater than the right
                if nums[l] <= target < nums[middle]: #has to be less than middle 
                    r = middle - 1 #shrink closer to the left
                else: 
                    l = middle + 1

            else:
                #means the middle to right is sorted, has to be in that area
                if nums[middle] < target <= nums[r]:
                    l = middle + 1 
                else: 
                    r = middle - 1
                    
        return -1


