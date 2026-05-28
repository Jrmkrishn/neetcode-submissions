class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = set()
        start = 0
        max_str = 0
        for end in range(0, len(s)):
            while s[end] in unique:
                unique.remove(s[start])
                start += 1
            max_str =  max(max_str,end-start+1)
            unique.add(s[end])
        return max_str