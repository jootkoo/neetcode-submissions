class Solution:
    def search(self, nums: List[int], target: int) -> int:
        middle = int(len(nums) / 2)
        if nums[middle] == target:
            return middle
        elif nums[middle] > target:
            while middle >= 0:
                if nums[middle] == target:
                    return middle
                else:
                    middle -=1
            return -1
        else:
            while middle <= len(nums) - 1:
                if nums[middle] == target:
                    return middle
                else:
                    middle +=1
            return -1
       

            