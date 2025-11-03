class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0 : return 0
        maxPrice = prices[0]
        minPrice = prices[0]
        profit = 0

        for i in prices:
            # Update min
            if i < minPrice : minPrice = i
            #update profit
            if i - minPrice > profit : profit = i - minPrice
        print(minPrice,maxPrice)
        if profit < 0 : return 0
        else : return profit
        
