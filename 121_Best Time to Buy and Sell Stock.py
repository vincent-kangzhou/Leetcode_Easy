class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<=1: return 0
        low=prices[0]
        max_profit=0
        for i in range(1, len(prices)):
            if prices[i]<low:
                low=prices[i]
            elif prices[i]-low>max_profit:
                max_profit=prices[i]-low
        
        return max_profit
        
