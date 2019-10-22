class Solution(object):
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        res=[0]*num_people
        res[0]=1
        
        c=2
        candies-=1
        i=1
        while candies>=c:
            res[i%num_people]+=c
            candies-=c
            c+=1
            i+=1
            
        if candies:
            res[i%num_people]+=candies
            
        return res
        
        
        
class Solution(object):
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        res=[0]*num_people
        count=1
        i=0
        while candies>=count:
            res[i%num_people]+=count
            candies-=count
            count+=1
            i+=1
  
            
        if candies:
            res[i%num_people]+=candies
        return res
        
        
        
class Solution(object):
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        res = [0] * num_people
        count = 1
        while candies > 0:
            inx = (count - 1) % num_people
            val = count if candies - count >= 0 else candies
            res[inx] += val
            candies -= val
            count += 1
        return res
