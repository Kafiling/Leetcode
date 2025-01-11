class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min = prices[0]
        temp = 0
        profit = 0
        i=0
        for p in prices:
            temp = p - min
            if temp > profit:
                profit = temp
            if min > p:
                min = p
        return profit
