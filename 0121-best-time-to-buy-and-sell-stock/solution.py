class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cheapest =  prices[0]
        ret = 0
        for price in prices: 
            if price < cheapest: 
                cheapest = price
            ret = max(ret, price-cheapest) 
        
        return ret 
