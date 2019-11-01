class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        res=[]
        for i in range(1, N+1):
            if self.validCheck(i):
                res.append(i)
                
        return len(res)
                
            
            
    def validCheck(self, digit):

        digits=[]
        while digit>0:
            digits.append(digit%10)
            digit=digit//10
        if sum([i in [3,4,7] for i in digits])>0:
            return False
        if sum([i in [0,1,8] for i in digits])==len(digits):
            return False
        return True
        
        
        
class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        count=0
        for digit in range(1, N+1):

            digits=[]
            while digit>0:
                digits.append(digit%10)
                digit=digit//10
            if sum([i in [3,4,7] for i in digits])>0:
                continue
            if sum([i in [0,1,8] for i in digits])==len(digits):
                continue
            count+=1
        return count
        
        
        
class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        count=0
        for digit in range(1, N+1):
            flag=True
            flag2=False

            digits=[]
            while digit>0:
                digits.append(digit%10)
                digit=digit//10
                
                
            for i in digits:
                if i in [3,4,7]:
                    flag=False
                    break
                    
                else:
                    
                    if i not in [0,1,8]:
                        flag2=True
                    else:
                        continue
                        
                    
            if flag and flag2:
                
                count+=1
        return count
        
        
        
        
class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        valid=[2,5,6,9]
        nonvalid=[3,4,7]
        
        def isGood(num):
            for y in nonvalid:
                if str(y) in str(num):
                    return False
                
            return any(str(i) in str(num) for i in valid)
        
        return sum(map(int, [isGood(num) for num in range(1, N+1)]))
        
        
class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """

        nonvalid=['3','4','7']
        
        dmap={'0':'0', '1':'1', '8':'8','2':'5','5':'2','6':'9','9':'6'}
        res=0
        
        for num in range(1,N+1):
            num_str=list(str(num))
            if any(i in num_str for i in nonvalid):
                continue
                
            num_map=map(lambda x: dmap[x], num_str)
            
            if num_map==num_str:
                continue
            res+=1
            
        return res
        
        
class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        valid=['2','5','6','9']
        nonvalid=['3','4','7']
        
        dmap={'0':'0', '1':'1', '8':'8','2':'5','5':'2','6':'9','9':'6'}
        res=0
        
        for num in range(1,N+1):
            num_str=list(str(num))
            if any(i in num_str for i in nonvalid):
                continue
  
            
            if any(i in valid for i in num_str ):
     
                res+=1
            
        return res
        
        
class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        valid=['2','5','6','9']
        nonvalid=['3','4','7']
        
        dmap={'0':'0', '1':'1', '8':'8','2':'5','5':'2','6':'9','9':'6'}
        res=0
        
        for num in range(1, N+1):
            num_str=list(str(num))
            
            if not (set(num_str)&(set(nonvalid))) and (set(num_str)&(set(valid))):
                res+=1
                
        return res
        
        
class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        dp=[0]*(10001)
        dp[0],dp[1],dp[8]=1,1,1
        dp[2],dp[5],dp[6],dp[9]=2,2,2,2
        count=0
        for i in range(1, N+1):
            div=i//10
            reminder=i%10
            dp[i]= 0 if dp[div]*dp[reminder]==0 else max(dp[div], dp[reminder])
            if dp[i]==2:
                count+=1
        return count
        
