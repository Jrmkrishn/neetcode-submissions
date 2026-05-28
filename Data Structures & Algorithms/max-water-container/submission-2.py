class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_product = 0
        while l < r:
            product = min(heights[l], heights[r]) * (r-l)
            max_product =  max(max_product, product)
            if heights[l] < heights[r]:
                l += 1
            else:
                r-=1
        return max_product   