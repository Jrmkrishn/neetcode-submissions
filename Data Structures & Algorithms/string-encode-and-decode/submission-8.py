class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            n = len(word)
            res += f'{n}#{word}'
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        print(s)
        while i < len(s):
            j = i
            while s[j] != "#":
                print(s[j])
                j += 1 
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i: j])
            i = j
        return res