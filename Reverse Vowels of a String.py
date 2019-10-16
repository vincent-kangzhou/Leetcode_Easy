class Solution:
    def reverseVowels(self, s: str) -> str:
        mapping='aeiouAEIOU'
        s=list(s)
        i=0
        j=len(s)-1
        
        while i<j:
            while (s[i] not in mapping and i<min(j, len(s)-1)):
                i+=1
            while (s[j] not in mapping and j>max(i,0)):
                j-=1
            s[i],s[j]=s[j],s[i]
            
            i+=1
            j-=1
        return ''.join(s)
