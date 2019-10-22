class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        import bisect
        arr1.sort()
        reminder=[]
        for num in arr1:
            if num not in arr2:
                reminder.append(num)
        reminder.sort()
            
        res=[]
        for i in arr2:
            left=bisect.bisect_left(arr1, i)
            right=bisect.bisect_right(arr1,i)
            
            res+=arr1[left:right]
            
        return res+reminder
            
            
        
        
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        left=[]
        right=[]
        import collections
        num_dict=collections.Counter(arr1)
        
        for i in arr2:
            left+=[i]*num_dict[i]
            
        reminder=set(arr1)-set(arr2)
        for i in reminder:
            right+=[i]*num_dict[i]

        right.sort()

        return left+right
        
        
        
        
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        left=[]
        right=[]
        dic={}
        
        for i in arr1:
            if i in arr2:
                dic[i]=dic.setdefault(i,0)+1
            else:
                right.append(i)
                
        for i in arr2:
            left+=[i]*dic[i]
            
        right.sort()
        
        return left+right
        
        
        
        
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        lookup = {v: i for i, v in enumerate(arr2)}
        return sorted(arr1, key=lambda i: lookup.get(i, len(arr2)+i))
