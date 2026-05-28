class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+", "-", "*", "/"}

        for ch in tokens:
            if ch not in operators:
                stack.append(int(ch))
            else:
                a = stack.pop()
                b = stack.pop()
                if ch == "+":
                    stack.append(a + b)
                elif ch == "-":
                    stack.append(b - a)
                elif ch == "*":
                    stack.append(a * b) 
                elif ch == "/":
                    stack.append(int(b / a))
                
        return stack[-1]