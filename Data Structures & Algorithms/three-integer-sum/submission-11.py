class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sort = sorted(nums) #sort the list
        result = [] # result reurn
        if sort[0] == 0 and sort[1] == 0 and sort[2] == 0: #if [0,0,0] only
            result.append([sort[0] , sort[1] , sort[2]])
            return result
        for i in range(len(sort)-2): #goes through each index
            #-2 otherwise the 2 pointers will equal the same value  
            l = i + 1 #left pointer is one infront of the index
            r = len(nums) - 1 #right pointer always at the end   
            while l < r: #while loop to move the pointers
                total = sort[i] + sort[l] + sort[r]
                
                if total < 0: #if total is less than 0 move left up
                    l += 1
                elif total > 0:
                    r -= 1
                else: #if found, move both pointers up / back one since found
                    if [sort[i] , sort[l] , sort[r]] in result:
                        l+= 1
                        r-=1 
                        continue
                    else:
                        result.append([sort[i] , sort[l] , sort[r]])
                        l+= 1
                        r-=1 
                
        return result






