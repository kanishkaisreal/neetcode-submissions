class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit  = 0 
        minprice  = prices[0]
        for price in prices:
            if price < minprice:
                minprice = price
            else:
                maxprofit = max(maxprofit, price - minprice)
        
        return maxprofit 