###Dynamic programming
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """

        totalCost=[0]*len(cost)
        totalCost[0]=cost[0]
        totalCost[1]=cost[1]
        
        for i in range(2, len(cost)-1):
            totalCost[i]=min(totalCost[i-2], totalCost[i-1])+cost[i]
        return min(totalCost[-2], totalCost[-3]+cost[-1])
        
        
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        
        # this is dynamic programming
        
        size=len(cost)
        dp=[cost[0]]*size
        dp[1]=cost[1]
        for i in range(2, size):
            dp[i]=min(dp[i-1], dp[i-2])+cost[i]
            
        return min(dp[-1], dp[-2])
            
            
            
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        
        # this is dynamic programming
        
        size=len(cost)

        pre, cur=cost[0], cost[1]

        for i in range(2, size):
            pre, cur= cur ,min(pre, cur)+cost[i]
            
        return min(pre, cur)
