class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i, j, k = 0, 1, len(nums) - 1
        output = set()
        nums.sort()
        while i < len(nums) - 2:
            total = nums[i] + nums[j] + nums[k]
            if j >= k:
                i += 1
                j = i + 1
                k = len(nums) - 1
            elif total == 0:
                output.add((nums[i], nums[j], nums[k]))
                j += 1
            elif total < 0:
                j += 1
            elif total > 0:
                k -= 1
            else:
                j += 1
                k -= 1
            
            
            
        return [list(x) for x in output]