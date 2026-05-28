class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:         
       res = [1] * len(nums) 
       prd = 1                                    
       for idx in range(1, len(nums)):
            res[idx] = prd * nums[idx - 1]
            prd = res[idx]
       prd = 1
       for idx in range(len(nums) - 1, -1, -1): 
         res[idx] *= prd
         prd = prd * nums[idx]
         print(prd, res)
       return res