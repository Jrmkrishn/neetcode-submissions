class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count_elem = {}
        for num in nums:
            if num in count_elem:
                return True
            else:
                count_elem[num] = 0
        return False