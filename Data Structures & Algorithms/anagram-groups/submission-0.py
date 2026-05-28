from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        maps = defaultdict(list)
        for string in strs:
            count = [0] * 26
            for c in string:
                count[ord(c) - ord("a")] += 1
            maps[tuple(count)].append(string)
        return maps.values()
