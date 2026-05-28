class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        start = 0
        maps = {}
        for end in range(len(s)):
            maps[s[end]] = maps.get(s[end], 0) + 1
            while (end - start + 1) - max(maps.values()) > k:
                maps[s[start]] -= 1
                start += 1
            res =  max(res, (end - start + 1))
        return res