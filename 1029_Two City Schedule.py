class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        len_=len(costs)//2
        dist=[i-j for i, j in costs]
        dist, costs=zip(*sorted(zip(dist, costs)))
        
        return sum(i for i,_ in costs[:len_])+sum(j for _,j in costs[len_:])
        
        
        
        
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        len_=len(costs)//2
        costs.sort(key=lambda x: x[0]-x[1])
        
        return sum(i for i,_ in costs[:len_])+sum(j for _,j in costs[len_:])
        
        
        
        
        
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        len_=len(costs)//2
        costs=sorted(costs, key=lambda x: x[0]-x[1])
        
        return sum(i for i,_ in costs[:len_])+sum(j for _,j in costs[len_:])
        
        
        
        
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:

        N = len(costs)//2
        ans = 0
        diffa, diffb = [], []

        for cost in costs:  # 贪心思想，进行处理
            if cost[0] < cost[1]:  # 去A城市
                ans += cost[0]     # 记录总的花费
                diffb.append(cost[1]-cost[0])  # 并记录如果去B城市，多花的钱，保存到 diffb
            else:                 # 同理，去B城市 ...
                ans += cost[1]
                diffa.append(cost[0]-cost[1])

        if len(diffa) < len(diffb):  # 分配到A城市的人多，则，从B里面，根据最优原则，选出几人，去B城市
            diffb.sort()
            for j in range(len(diffb)-N):
                ans += diffb[j]

        if len(diffa) > len(diffb):  # 同理，分配到B城市的人多 ...
            diffa.sort()
            for i in range(len(diffa)-N):
                ans += diffa[i]

        return ans
