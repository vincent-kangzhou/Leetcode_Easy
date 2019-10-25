class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        A=set()
        B={i:[] for i in range(1,N+1)}
        
        for i in range(len(trust)):
            m,n=trust[i]
            A.add(m)
            B[n].append(m)
            
        if len(A)==N: return -1
        candidates=set(range(1,N+1))-A
        for j in candidates:
            if len(B[j])==N-1:
                return j
        return -1
        
        
class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """

        graph={i:[] for i in range(1,N+1)}
        
        for i in range(len(trust)):
            graph[trust[i][0]].append(trust[i][1])
        
        for k in graph:
            if len(graph[k])==0:
                judge=k
                
                for person in graph:
                    if person!=judge and judge not in graph[person]:
                        return -1
                return judge
        return -1
        
        
        
        
class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        stat=[0]*N
        
        for x, y in trust:
            stat[y-1]+=1
            stat[x-1]-=1
            
        for idx, val in enumerate(stat):
            if val==N-1:
                return idx+1
        return -1
