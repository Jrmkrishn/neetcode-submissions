class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_word = defaultdict(list)
        for word in strs:
            mapping= [0] * 26
            for ch in word:
                mapping[ord(ch) - 97] += 1
            dict_word[tuple(mapping)].append(word)
        return dict_word.values()