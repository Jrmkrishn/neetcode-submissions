class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {"[" : "]", "(" : ")", "{" : "}" }
        for ch in s:
            if ch in brackets.keys():
                stack.append(ch)
            else:
                if not stack:
                    return False
                elem = stack.pop()
                if brackets[elem] == ch:
                    continue
                else:
                    return False 
        return len(stack) == 0



