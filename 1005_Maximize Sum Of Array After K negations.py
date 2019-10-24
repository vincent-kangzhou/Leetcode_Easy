class Solution(object):
    def largestSumAfterKNegations(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        sum_=sum(A)
        A.sort()

        
        
        if A[-1]<=0:
            return sum_-2*sum(A[:K])
        if A[0]>=0:
            return sum(A[1:])+(-1)**K*A[0]
        import bisect
        idx_left=bisect.bisect_left(A,0)


        if idx_left>=K:

            return sum_-2*sum(A[:K])
        else:
            if 0 in A:
            
       
                return sum_-2*sum(A[:idx_left])
            else:
                reminder=(K-idx_left)%2
                if reminder==0:
                    return sum_-2*sum(A[:idx_left])
                else:
                    if abs(A[idx_left-1])>=abs(A[idx_left]):
                        return sum_-2*sum(A[:idx_left])-2*(A[idx_left])
                    else:
                        return sum_-2*sum(A[:idx_left])+2*(A[idx_left-1])
                
                
                
                
class Solution(object):
    def largestSumAfterKNegations(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        import heapq
        _sum=sum(A)
        heapq.heapify(A)
        while K>0:
            curmin=heapq.heappop(A)
            heapq.heappush(A,-curmin)
            _sum+=-curmin*2
            
            K-=1
            
        return _sum
        
        
        
        
   class Solution(object):
    def largestSumAfterKNegations(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        
        A.sort()
        
        res=0
        lastMin=10001
        for i in A:
            if K==0:
                res+=i
            elif i<0:
                res+=(-i)
                K-=1
                lastMin=min(lastMin, -i)
                
            else:
                K=K%2
                if K==1:
                    if lastMin<i:
                        res-=2*lastMin
                        res+=i
                    else:
                        res-=i
            
                else:
                    res+=i
                K=0
                
                
                
                
         class Solution(object):
    def largestSumAfterKNegations(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        
        A.sort()
        i=0
        
        while  i<K and A[i]<0:
            A[i]=-A[i]
            i+=1
            
        return sum(A)-(K-i)%2*min(A)*2       

        return res     
