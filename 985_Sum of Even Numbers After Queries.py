class Solution(object):
    def sumEvenAfterQueries(self, A, queries):
        """
        :type A: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        count=0
        for i in A:
            if i%2==0:
                count+=i
        
        res=[]
        
        
        for val, idx in queries:
            if A[idx]%2==0:
                if val%2==0:
                    res.append(count+val)
                else:
                    res.append(count-A[idx])
            else:
                if val%2==0:
                    res.append(count)
                else:
                    res.append(count+A[idx]+val)
            count=res[-1]
            A[idx]+=val
        return res
        
        
        
class Solution(object):
    def sumEvenAfterQueries(self, A, queries):
        """
        :type A: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        res=[]
        count=None
        for val, idx in queries:
            before=A[idx]
            A[idx]+=val
            after=A[idx]
            
            if count==None:
                count=sum(filter(lambda x: x%2==0, A))
            else:
                if before%2==0:
                    count-=before
                if after%2==0:
                    count+=after
            res.append(count)
        return res
        
        
        
class Solution(object):
    def sumEvenAfterQueries(self, A, queries):
        """
        :type A: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        res=[]
        count=sum(x for x in A if x%2==0)
        
        for val, idx in queries:
            if A[idx]%2==0:
                count-=A[idx]
            A[idx]+=val
            
            if A[idx]%2==0:
                count+=A[idx]
            res.append(count)
        return res
                
