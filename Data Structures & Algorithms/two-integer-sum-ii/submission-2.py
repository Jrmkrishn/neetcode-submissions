class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        maps = {}
        for idx, num in enumerate(numbers):
            if target-num in maps:
                return [maps[target-num]+1, idx+1]
            maps[num] = idx
        return []