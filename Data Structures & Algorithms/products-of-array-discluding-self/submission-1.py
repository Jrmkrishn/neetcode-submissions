class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prev = 1
        result=[]
        for idx, num in enumerate(nums):
            result.append(prev)
            prev *= num
        prev = 1
        for idx in range(len(nums)-1,-1,-1):
            result[idx] *= prev
            prev *= nums[idx]
        return result