class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        noDupes = set(nums)
        total = 1

        if len(nums) == 0:
                return 0

        for i,n in enumerate(noDupes): #find the start
            if n-1 not in noDupes and n+1 in noDupes:
                starts = n
                result = 1
                while starts+1 in noDupes:
                    if starts+1 in noDupes:
                        result +=1
                        starts +=1
                        total = max(total, result)
        return total

                    

        