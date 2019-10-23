import collections
class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A)!=len(B): return False
        

        
        A_diff={}
        
        B_diff={}
        
        
        for idx, val in enumerate(A):
            if val!=B[idx]:
                A_diff[idx]=val
                B_diff[idx]=B[idx]
                

        if len(A_diff)==2:
            key=list(A_diff.keys())
            
            if A_diff[key[0]]==B_diff[key[1]] and A_diff[key[1]]==B_diff[key[0]]:
                return True

            
        if len(A_diff)==0 and len(A)>0:
            if max(collections.Counter(list(A)).values())>=2:
                return True

        return False
                
