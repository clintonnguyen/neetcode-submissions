class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start, end = 0, len(prices) - 1
        minPrice = 100
        maxProfit = 0
        for i in range(len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]
            if prices[i] - minPrice > maxProfit:
                maxProfit = prices[i] - minPrice
        return maxProfit

