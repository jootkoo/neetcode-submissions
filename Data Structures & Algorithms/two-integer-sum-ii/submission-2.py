class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashm = {}
        for i, n in enumerate(numbers):
            diff = target - n
            if diff in hashm:
                return [hashm[diff]+1, i+1]
            hashm[n] = i