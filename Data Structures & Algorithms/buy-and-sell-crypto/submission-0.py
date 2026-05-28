class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start = 0
        max_P = 0
        for end in range(1, len(prices)):
            if prices[end] > prices[start]:
                max_P = max(max_P, prices[end] - prices[start])
            else:
                start = end
        return max_P