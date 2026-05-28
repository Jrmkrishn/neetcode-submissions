class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        min_elem = self.stack[0]
        for num in self.stack:
            min_elem = min(min_elem, num)
        return min_elem 
