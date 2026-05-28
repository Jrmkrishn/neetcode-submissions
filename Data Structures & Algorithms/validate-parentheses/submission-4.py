class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {"[" : "]", "(" : ")", "{" : "}" }
        for ch in s:
            if ch in brackets:
                stack.append(ch)
            else:
                if not stack or brackets[stack.pop()] != ch:
                    return False 
        return not stack



