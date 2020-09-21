class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        minPrice, cost = float('inf'), 0
        for i in range(len(prices)):
            if minPrice >= prices[i]:
                minPrice = prices[i]
            if prices[i]-minPrice > cost:
                cost = prices[i]-minPrice
        return cost