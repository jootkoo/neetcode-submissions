class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i,x in enumerate(nums):
            goal = target - x
            if goal in seen:
                return [seen[goal], i]
            seen[x] = i