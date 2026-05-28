class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        maxLeft, maxRight = height[l], height[r]
        summ = 0
        while l < r:
            if maxLeft < maxRight:
                l += 1
                maxLeft = max(maxLeft, height[l])
                summ += maxLeft - height[l]
            else:
                r -= 1
                maxRight = max(maxRight, height[r])
                summ += maxRight - height[r]
        return summ


