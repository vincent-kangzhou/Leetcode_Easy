class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        dist=0
        exist=False
        
        for idx, val in enumerate(seats):
            if not exist and val==0:
                exist=True
                start=idx
            elif exist and val==1:
                res=((idx-start)+1)//2
                
                dist=max(dist, res)
                
                exist=False
        if seats[0]==0:
            dist=max(dist, seats.index(1))
        if seats[-1]==0:
            dist=max(dist, seats[::-1].index(1))
        return dist
        
        
        
        
        
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        prev=-1
        dist=0
        
        for idx, val in enumerate(seats):
            if val:
                if prev<0:
                    dist=idx
                else:
                    dist=max(dist, (idx-prev)//2)
                    
                prev=idx
        return max(dist, len(seats)-1-prev)
