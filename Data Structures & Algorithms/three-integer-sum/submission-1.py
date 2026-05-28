class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for idx, num in enumerate(nums):
            l, r = idx + 1, len(nums) - 1
            if idx > 0 and nums[idx] == nums[idx-1]:
                    continue
            while l < r:
                threeSum  = num + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    result.append([num, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1

            
        return result
