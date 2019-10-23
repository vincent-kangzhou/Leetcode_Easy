class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        num_=sorted([a,b,c])

            
        if min(num_[2]-num_[1],num_[1]-num_[0])>2:
            minimum=2
            
        elif max(num_[2]-num_[1],num_[1]-num_[0])>1:
            minimum=1
        else:
            minimum=0
            
        maximum= (num_[2]-num_[1]-1)+(num_[1]-num_[0]-1)
        
        return [minimum, maximum]
        
        



class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        a,b,c=sorted([a,b,c])
        if a==b-1 and b==c-1: minv=0
        elif b-a<=2 or c-b<=2: minv=1
        else: minv=2
        
        maxv=(b-a-1)+(c-b-1)
        
        return [minv,maxv]
        
        
        
        
        
class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        minimum = min([a,b,c])
        maximum = max([a,b,c])

        if (maximum - minimum) == 2:
            return [0,0]
        elif abs(a-b) == 1 and abs(b-c) == 1:
            return [0, maximum - minimum - 2]
        elif abs(a-b) in [1,2] or abs(b-c) in [1,2] or abs(a-c) in [1,2]:
            return [1, maximum - minimum - 2]
        else:
            return [2, maximum - minimum - 2]
