class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            sum_num = numbers[l] + numbers[r]
            print(sum_num)
            if target == sum_num:
                return [l+1, r+1]
            elif target > sum_num:
                l += 1
            else:
                r -= 1
        return []