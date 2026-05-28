class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value_store = {}
        for idx, num in enumerate(nums):
            if (target - num) in value_store:
                return [value_store[target-num], idx]
            value_store[num] = idx