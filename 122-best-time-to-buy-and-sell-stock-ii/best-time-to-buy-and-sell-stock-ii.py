class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 1000000
        sell = 0
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < sell:
                max_profit += sell - buy
                buy = 1000000
                sell = 0
            else:
                sell = prices[i]
                if i == len(prices) - 1 and sell > buy:
                    max_profit += sell - buy
            if prices[i] < buy:
                buy = prices[i]
            
        return max_profit
                
            