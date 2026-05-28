class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch == "[" or ch == "(" or ch == "{":
                stack.append(ch)
            else:
                if not stack:
                    return False
                elem = stack.pop()
                if (elem == "[" and ch == "]") or (elem == "{" and ch == "}") or elem == "(" and ch == ")" :
                    continue
                else:
                    return False
        return len(stack) == 0



