class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        dic={i:[] for i in range(60)}
        for i in range(len(time)):
            dic[time[i]%60].append(i)
        count=0
            
        for i in range(1,30):
            count+=(len(dic[i])*len(dic[60-i]))
        if len(dic[0])>1:
                    
            count=count+len(dic[0])*(len(dic[0])-1)//2
        if len(dic[30])>1:
            
            count=count+len(dic[30])*(len(dic[30])-1)//2
                    
        return count
        
        
        
        
class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        import collections
        dic=collections.defaultdict(int)
        for i in range(len(time)):
            dic[time[i]%60]+=1
        count=0
            
        for i in range(1,30):
            count+=(dic[i]*dic[60-i])
        if dic[0]>1:
                    
            count=count+dic[0]*(dic[0]-1)//2
        if dic[30]>1:
            
            count=count+dic[30]*(dic[30]-1)//2
                    
        return count
            
