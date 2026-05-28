class Solution:
    def trap(self, height: List[int]) -> int:
       maxLeft = [0] * len(height)
       maxRight = [0] * len(height)
       minHeight = [0] * len(height)
       summ = 0
       for idx in range(1, len(height)):
            print(maxLeft[idx - 1], height[idx-1])
            maxLeft[idx] = max(maxLeft[idx - 1], height[idx - 1])
       for idx in range(len(height)-2, -1, -1):
            maxRight[idx] = max(maxRight[idx + 1], height[idx + 1])
       for idx in range(len(height)):
            minHeight[idx] = min(maxLeft[idx], maxRight[idx])
       print(minHeight)
       for idx in range(len(height)):
            if minHeight[idx] - height[idx] > 0:
                summ += minHeight[idx] - height[idx]
       return summ




