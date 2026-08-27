class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for x in tokens:
            if x == '+' or x == '-' or x == '*' or x == '/':
                total = 0

                num2 = stack[-1]
                stack.pop()
                num1 = stack[-1]
                stack.pop()


                if x == '+':
                    total = num1+num2
                elif x == '-':
                    total = num1-num2
                elif x == '*':
                    total = num1*num2
                else: #if x = /
                    total = int(num1/num2) #using int removes the decimal
                stack.append(total)

            else:
                stack.append(int(x))
        return stack[0]
                