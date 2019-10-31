class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        import itertools
        maxArea=0
        for point in itertools.permutations(points, 3):
            area=self.areaCal(point[0],point[1],point[2])
            if area>maxArea:
                maxArea=area
        return maxArea 
    
    def areaCal(self, p1, p2, p3):
        return 0.5*abs(p1[0]*(p3[1]-p2[1])+p2[0]*(p1[1]-p3[1])+p3[0]*(p2[1]-p1[1]))
        
        
class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """

        maxArea=0
        for i in range(len(points)-2):
            for j in range(i+1, len(points)-1):
                for k in range(i+2, len(points)):
                    area=self.areaCal(points[i],points[j],points[k])
                    if area>maxArea:
                        maxArea=area
        return maxArea 
    
    def areaCal(self, p1, p2, p3):
        return 0.5*abs(p1[0]*(p3[1]-p2[1])+p2[0]*(p1[1]-p3[1])+p3[0]*(p2[1]-p1[1]))
    
