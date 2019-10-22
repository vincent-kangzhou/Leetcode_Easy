class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        len_=len(arr)
        idx=[]
        for i,val in enumerate(arr):
            if val==0:
                idx.append(i)
        offset=1
        for j in idx:
            idxx=j+offset
            offset+=1
            arr.insert(idxx,0)
            arr.pop()
            
            
            
            
class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        len_=len(arr)
        
        idx=0
        while idx<len_:
            if arr[idx]!=0:
                idx+=1
            else:
                arr.insert(idx,0)
                arr.pop()
                idx+=2
