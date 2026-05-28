class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l <= r:
            num_sum = numbers[l] + numbers[r]
            if target == num_sum:
                return [l+1, r+1]
            if target > num_sum:
                l += 1
            if target < num_sum:
                r -= 1
        return -1