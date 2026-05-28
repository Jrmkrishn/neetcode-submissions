class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:         
       res = [1] * len(nums) 
       prd = 1                                    
       for idx in range(len(nums)):
            res[idx] = prd 
            prd *= nums[idx]
       prd = 1
       for idx in range(len(nums) - 1, -1, -1): 
         res[idx] *= prd
         prd *= nums[idx]
         print(prd, res)
       return res