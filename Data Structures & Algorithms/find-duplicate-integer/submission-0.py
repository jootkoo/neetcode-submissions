class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashm = {}

        for i,n in enumerate(nums):
            if n in hashm:
                return n
            else:
                hashm[n] = n
