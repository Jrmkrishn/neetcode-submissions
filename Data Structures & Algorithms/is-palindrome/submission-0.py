class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr = s.split(" ")
        return "".join(c for wor in arr for c in wor if c.isalnum()).lower() == "".join(c for wor in arr for c in wor if c.isalnum()).lower()[::-1]