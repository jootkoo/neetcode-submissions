class Solution:
    def isValid(self, s: str) -> bool:
        closedToOpen = {")" : "(", "]" : "[", "}" : "{"}
        stack = []

        for char in s:
            if s[0] in closedToOpen:
                return False
            if char in closedToOpen:
                if stack and stack[-1] == closedToOpen[char]:
                    stack.pop()
                else:
                    return False
                
            else:
                stack.append(char)
        if stack:
            return False
        else:
            return True