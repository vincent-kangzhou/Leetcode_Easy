class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        dist={}
        for i in range(R):
            for j in range(C):
                dist[(i,j)]=abs(i-r0)+abs(j-c0)
                
        dist=sorted(dist,key=dist.get)
        
        return [i for i in dist]
        
        
        
class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        ans, dist = [], []
        for r in range(R):
            for c in range(C):
                dist += [abs(r - r0) + abs(c - c0)]
                ans += [[r, c]]
        dist, ans = zip(*sorted(zip(dist, ans)))
        return ans
        
        
        
class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        def dist(point):
            pi, pj = point
            return abs(pi - r0) + abs(pj - c0)

        points = [(i, j) for i in range(R) for j in range(C)]
        return sorted(points, key=dist)	
