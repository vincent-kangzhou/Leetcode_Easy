class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        if not S: return [S]
        
        rest=self.letterCasePermutation(S[1:])
        
        if S[0].isalpha():
            return [S[0].lower()+i for i in rest]+[S[0].upper()+i for i in rest]
        
        return [S[0]+i for i in rest]
        
        
        
class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        ans = []
 
        def dfs(S, i, n):
            if i == n:
                ans.append(''.join(S))
                return
      
            dfs(S, i + 1, n)      
            if not S[i].isalpha(): return      
            S[i] = chr(ord(S[i]) ^ (1<<5))
            dfs(S, i + 1, n)
            S[i] = chr(ord(S[i]) ^ (1<<5))
    
        dfs(list(S), 0, len(S))
        return ans
        
        
class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        res=[]
        self.dfs(0, S.lower(), '',res)
        
        return res
        
    def dfs(self, pos, s, temp, res):
        if pos==len(s):
            res.append(temp)
            return
        self.dfs(pos+1, s, temp+s[pos], res)
        
        if s[pos].isalpha():
            self.dfs(pos+1, s, temp+s[pos].upper(),res)
            
            
class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        cur_s=[S]
        
        for i in range(len(S)):
            next_s=[]
            for s in cur_s:
                if s[i].isdigit():
                    next_s.append(s)
                
                else:
                    next_s.append(s[:i]+s[i].lower()+s[i+1:])
                    next_s.append(s[:i]+s[i].upper()+s[i+1:])
            cur_s=next_s
        return cur_s
                
                
                
class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        
        res=['']
        for s in S:
            if s.isalpha():
                res=[path+letter for path in res for letter in [s.upper(), s.lower()]]
            else:
                res=[path+s for path in res]
        return res
            
