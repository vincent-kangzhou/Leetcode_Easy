class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bulls=0
        cow1=[]
        cow2=[]
        for i in range(len(secret)):
            if secret[i]==guess[i]:
                bulls+=1
                
            else:
                cow1.append(secret[i])
                cow2.append(guess[i])
        cow=0
        for j in cow1:
            if j in cow2:
                cow+=1
                cow2.remove(j)
                
        return str(bulls)+'A'+str(cow)+'B'
        
        
        
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        import collections
        bulls=0
        cows=0
        secret_dict=collections.defaultdict(int)
        for s,g in zip(secret, guess):
            if s==g:
                bulls+=1
            else:
                secret_dict[s]+=1
                
        for idx, val in enumerate(guess):
            if val!=secret[idx] and secret_dict[val]:
                cows+=1
                secret_dict[val]-=1
                
        return str(bulls)+'A'+str(cows)+'B'
        
        
        
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bulls=0
        cows=0
        se=[0]*10
        gu=[0]*10
        for s, g in zip(secret, guess):
            if s==g:
                bulls+=1
            else:
                se[int(s)]+=1
                gu[int(g)]+=1
                
        for i in range(10):
            cows+=min(se[i],gu[i])
        return str(bulls)+'A'+str(cows)+'B'
        
        
        
