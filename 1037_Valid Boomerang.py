class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        if (points[0][0]==points[1][0] and points[0][1]==points[1][1]) or (points[0][0]==points[2][0] and points[0][1]==points[2][1]) or (points[1][0]==points[2][0] and points[1][1]==points[2][1]):
            return False
        
        return (points[2][1]-points[0][1])*(points[2][0]-points[1][0])!=(points[2][1]-points[1][1])*(points[2][0]-points[0][0])
