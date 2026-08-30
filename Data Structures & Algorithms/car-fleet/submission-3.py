class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        fleets = 1
        for i in range(len(position)):
            dest = (target - position[i]) / speed[i]
            stack.append([position[i], dest])
        stack.sort() #sorts by pos (smallest to largest)
        pos, time = stack.pop() #closest car to dest
        while stack:
            if stack[-1][1] <= time: # if car in front is slower than car behind
                stack.pop()
                
            else: #if car slow than car in front
                fleets +=1
                pos, time = stack.pop()

        return fleets