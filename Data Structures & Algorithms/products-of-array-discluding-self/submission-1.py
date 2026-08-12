class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        

        after = 1
        for x in range(len(nums)):
            result[x] = after #having this first skips the first val
            after *= nums[x] # this value will go to the next index.
            # for [1,2,3,4] if at 2, index 2 is 1*2 index 3 will be 1*2*3

        before = 1
        for x in range(len(nums)-1, -1, -1): #iterate backwards to multiply other side
            result[x] *= before
            before *= nums[x]
        return result


                
