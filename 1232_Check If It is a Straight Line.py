class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        
        x0,y0=coordinates[0]
        x1, y1=coordinates[1]
        
        if x0==x1:
            for i in range(2, len(coordinates)):
                if coordinates[i][0]!=x0:
                    return False
                
            return True
        
        a=(y1-y0)/(x1-x0)
        b=(y1-a*x1)
        
        for i in range(2, len(coordinates)):
            if coordinates[i][1]!=a*coordinates[i][0]+b:
                return False
            
        return True
                    
                    
                    
                    
                    
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        
        x0,y0=coordinates[0]
        x1, y1=coordinates[1]
        

        
        a=(y1-y0)/(x1-x0) if x1!=x0 else 0
        b=(y1-a*x1)
        
        for i in range(2, len(coordinates)):
            if x0==x1:
                if coordinates[i][0]!=x0:
                    return False
            
            if coordinates[i][1]!=a*coordinates[i][0]+b:
                return False
            
        return True
                    
                    
                    
                    
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        
        return all((coordinates[1][1]-coordinates[0][1])*(x-coordinates[0][0])==(y-coordinates[0][1])*(coordinates[1][0]-coordinates[0][0]) for x,y in coordinates[2:])
        
