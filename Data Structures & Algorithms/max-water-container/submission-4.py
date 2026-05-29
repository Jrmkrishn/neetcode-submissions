class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_sum = 0
        l,  r = 0, len(heights) - 1
        while l < r:
            min_num = min(heights[l], heights[r])
            total = (r -l) * min_num
            if total  > max_sum:
                max_sum = total
            if  heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return max_sum
