class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        res=[0]*N
        graph=[[] for i in range(N)]
        
        for path in paths:
            graph[path[0]-1].append(path[1]-1)
            graph[path[1]-1].append(path[0]-1)
            
        for i in range(N):
            neighbor_colors=[]
            for neighbor in graph[i]:
                neighbor_colors.append(res[neighbor])
            for color in range(1,5):
                if color in neighbor_colors:
                    continue
                else:
                    res[i]=color
        return res
        
        
        
        
class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        res=[0]*(N+1)
        
        res[1]=1
        
        dic={}
        
        for v1,v2 in paths:
            dic[v1]=dic.setdefault(v1,[])+[v2]
            dic[v2]=dic.setdefault(v2,[])+[v1]
            
        for i in range(2,N+1):
            if i not in dic:
                res[i]=1
            else:
                choice=[1,2,3,4]
                
                for neighbor in dic[i]:
                    if res[neighbor]==0:
                        continue
                    
                    else:
                        if res[neighbor] in choice:
                            idx=choice.index(res[neighbor])
                            del choice[idx]
                            
                res[i]=choice[0]
                
        return res[1:]
        
