class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = defaultdict(list)
        for word in strs:
            val = [0] * 26
            for ch in word:
                val[ord(ch) - ord('a')] += 1
            store[tuple(val)].append(word)
        return list(store.values())