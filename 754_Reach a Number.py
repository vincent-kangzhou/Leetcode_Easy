class Solution(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        target_abs=abs(target)
        import numpy
        step=int((numpy.sqrt(8*target_abs+1)-1)//2)
        
        total_step=(step+1)*step//2
        if total_step==target_abs:
            return step
            
        if ((target_abs-total_step)%2) and (step%2):
            return step+2
        if not ((target_abs-total_step)%2) and not (step%2):
            return step+3
        if ((target_abs-total_step)%2)!=(step%2):
            return step +1
            
            
class Solution(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        target_abs=abs(target)
        
        step=0
        while step*(step+1)< 2*target_abs:
            step+=1
        
        
        total_step=(step+1)*step//2
        if total_step==target_abs:
            return step
        step-=1
        total_step=(step+1)*step//2
            
        if ((target_abs-total_step)%2) and (step%2):
            return step+2
        if not ((target_abs-total_step)%2) and not (step%2):
            return step+3
        if ((target_abs-total_step)%2)!=(step%2):
            return step +1
            
            
            
class Solution(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        target_abs=abs(target)
        
        step=0
        while step*(step+1)< 2*target_abs:
            step+=1
        
        
        total_step=(step+1)*step//2
        if total_step==target_abs:
            return step
        elif (total_step-target_abs)%2==0:
            return step
        else:
            if (step%2==0):
                return step+1
            else:
                return step+2
                
                
                
class Solution(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        target=abs(target)
        k=0
        sum_=0
        while sum_<target:
            k+=1
            sum_+=k
        d=abs(sum_-target)
        if not d&1:
            return k
        return k+1 +(k%2)
