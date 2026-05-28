class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_word = defaultdict(list)
        for word in strs:
                dict_word[tuple(sorted(word))].append(word)
        return dict_word.values()            