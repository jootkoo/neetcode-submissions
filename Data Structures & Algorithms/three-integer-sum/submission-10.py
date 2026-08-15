class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sort = sorted(nums)
        result = []
        if sort[0] == 0 and sort[1] == 0 and sort[2] == 0:
            result.append([sort[0] , sort[1] , sort[2]])
            return result
        for i in range(len(sort)):
            l = i + 1
            r = len(nums) - 1
            if l >= r:
                break        
            while l < r:
                total = sort[i] + sort[l] + sort[r]
                
                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    if [sort[i] , sort[l] , sort[r]] in result:
                        l+= 1
                        r-=1 
                        continue
                    else:
                        result.append([sort[i] , sort[l] , sort[r]])
                        l+= 1
                        r-=1 
                
        return result






