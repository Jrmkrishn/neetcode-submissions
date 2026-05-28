class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        maps = {}
        for idx, num in enumerate(nums):
            if (target - num) in maps:
                return [maps[target-num], idx]
            maps[num] = idx
        return []