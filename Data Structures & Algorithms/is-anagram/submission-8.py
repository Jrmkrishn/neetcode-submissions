class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_map = {}
        t_map = {}
        for ch1, ch2 in zip(s, t):
            s_map[ch1] = s_map.get(ch1, 0) + 1
            t_map[ch2] = t_map.get(ch2, 0) + 1

        return s_map == t_map