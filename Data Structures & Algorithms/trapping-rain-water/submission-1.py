class Solution:
    def trap(self, height: List[int]) -> int:
        max_prefix  = 0
        prefix = [0]*(len(height)-1)
        max_suffix = 0
        suffix = [0]*(len(height)-1)
        max_sum = 0
        for idx in range(1, len(height) - 1):
            max_prefix = max(max_prefix, height[idx-1])
            prefix[idx] =  max_prefix

        for idx in range(len(height)-2, -1, -1):
            max_suffix = max(max_suffix, height[idx+1]) 
            suffix[idx] =  max_suffix
        
        for idx in range(len(height)-1):
            total = min(prefix[idx], suffix[idx]) - height[idx]
            if total > 0:
                max_sum += total
        return max_sum