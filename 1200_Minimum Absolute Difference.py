class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr.sort()
        diff=[arr[i]-arr[i-1] for i in range(1,len(arr))]
        
        res=[]
        min_=min(diff)
        for idx, val in enumerate(diff):
            if val==min_:
                res.append([arr[idx],arr[idx+1]])
        
        return res
        
        
class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        
        arr.sort()
        res=[]
        min_diff=float('inf')
        for i in range(1, len(arr)):
            if arr[i]-arr[i-1]<min_diff:
                res=[[arr[i-1],arr[i]]]
                min_diff=arr[i]-arr[i-1]
            elif arr[i]-arr[i-1]==min_diff:
                res.append([arr[i-1],arr[i]])
                
        return res
