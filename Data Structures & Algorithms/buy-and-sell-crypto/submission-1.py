class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start = maxProfit = 0
        for end in range(0, len(prices)):
            maxProfit = max(maxProfit, prices[end] - prices[start])
            if prices[start] > prices[end]:
                start = end
        return maxProfit