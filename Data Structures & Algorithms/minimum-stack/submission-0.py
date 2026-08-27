class MinStack:

    def __init__(self):
        self.stack = []
        self.mini = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.mini) == 0:
            self.mini.append(val)
        else:
            val = min(val, self.mini[-1]) #compare the val and the top of min stack
            self.mini.append(val)


    def pop(self) -> None:
        if len(self.stack) == 0:
            return None
        else:
            self.stack.pop()
            self.mini.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.mini[-1]
