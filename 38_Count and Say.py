class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        res='1'
        
        for j in range(n-1):
            new_res=''
            count=1
            for i in range(len(res)-1):
                if res[i]==res[i+1]:
                    count+=1
                else:
                    new_res+=str(count)+str(res[i])
                    count=1
                    
            if count==1:
                new_res+=str(1)+str(res[-1])
            else:
                new_res+=str(count)+str(res[i])
            res=new_res
        return res
        
        
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        res='1'
        
        for i in range(n-1):
            new_res, pre, count='',res[0],0
            for j in range(len(res)):
                if res[j]==pre:
                    count+=1
                    
                else:
                    new_res+=str(count)+str(pre)
                    count=1
                    pre=res[j]
                    
            new_res+=str(count)+str(pre)
            res=new_res
            
        return res
        
        
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        res='1'
        for i in range(n-1):
            res=''.join([str(len(list(group)))+digits for digits, group in itertools.groupby(res)])
            
        return res
                    
