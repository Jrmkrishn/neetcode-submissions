class Solution:

    def encode(self, strs: List[str]) -> str:
        res = "" 
        for word in strs:
            res += f"{len(word)}#{word}"
        return res
    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        idx = 0
        while idx <= len(s) - 1:
            print(idx, len(s))
            if s[idx] == "#":
                n = int(s[i:idx]) + 1
                res.append(s[idx + 1: idx +n])
                i = idx + n 
                idx = i
            else:
                idx += 1
        return res