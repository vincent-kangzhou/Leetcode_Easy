class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        left, right=0,0
        remove=[]
        name=list(name)
        typed=list(typed)
        
        while left <len(name) and right<len(typed):
            
            if name[left]!=typed[right]:
                if len(remove)==0:
                    return False
                elif remove[-1]==typed[right]:
                    right+=1
                    continue
                else:
                    return False
                
            else:
                remove.append(name[left])
                left+=1
                right+=1
                
                
        return remove==name
        
        
        
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        
        N=len(name)
        T=len(typed)
        
        n,t=0,0
        
        while n<N:
            ci=name[n]
            
            countn=0
            
            countt=0
            while n<N and name[n]==ci:
                countn+=1
                n+=1
            while t<T and typed[t]==ci:
                countt+=1
                t+=1
                
            if countt<countn:
                return False
        return True
        
        
        
        
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        idx=0
        for i in range(len(typed)):
            if idx<len(name) and name[idx]==typed[i]:
                idx+=1
            elif i==0 or typed[i]!=typed[i-1]:
                return False
            
        return idx==len(name)
        
        
        
        
        
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        import re
        tsz=len(typed)
    
        
        idx=0
        
        str=name[0]
        for i in range(1, len(name)):
            if name[i-1]==name[i]:
                str+=name[i]
            else:
                match=re.match(str+'+',typed[idx:])
                
                if not match:
                    return False
                else:
                    str=name[i]
                    idx+=match.end()
                if idx>tsz-1:
                    return False
        
        return True and name[-1]==typed[-1]
        
        
        
        
        
        class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        nsz=len(name)
        tsz=len(typed)
        
        i=0
        str=''
        for j in range(tsz):
            if i<nsz and name[i]==typed[j]:
                i+=1
                str=name[i-1]
            elif typed[j]==str:
                continue
            else:
                
                return False
        return i==nsz
