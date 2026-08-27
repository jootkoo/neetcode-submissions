class Solution:
    def isValid(self, s: str) -> bool:
        closedToOpen = {")" : "(", "]" : "[", "}" : "{"}
        stack = []

        for x in s:
            if x in closedToOpen:
                if stack and stack[-1] == closedToOpen[x]:
                    stack.pop()
                else:
                    return False #this means if theres a clseod bracket w no start
            else:
                stack.append(x)
        return True if not stack else False

            