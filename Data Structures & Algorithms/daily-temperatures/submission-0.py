class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result= [0] * len(temperatures) #initialize so if not found 0 is alrdy there
        stack = [] # temp , index
        for i,n in enumerate(temperatures):
            while stack and n > stack[-1][0]: # the value is greater thn top stack v
                stackT, stackInd = stack.pop() #pop the temp and index
                result[stackInd] = (i - stackInd)
            stack.append([n, i])
        return result
