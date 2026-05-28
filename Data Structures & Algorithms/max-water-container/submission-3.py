class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        l, r = 0, len(heights) - 1
        while l < r:
            temp = (r-l) * min(heights[l], heights[r])
            area = max(area, temp)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return area