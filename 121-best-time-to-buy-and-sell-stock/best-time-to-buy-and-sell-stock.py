class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_ = prices[0]
        max_profit = 0 
        for i in range(1, len(prices)):
            if prices[i] - min_ > max_profit:
                max_profit = prices[i] - min_
            if prices[i] < min_:
                min_ = prices[i]
        return max_profit
