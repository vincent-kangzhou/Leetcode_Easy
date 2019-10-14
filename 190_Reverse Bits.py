class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res=0
        for i in range(32):
            res<<=1
            res |= ((n>>i)&1)
        return res
      
      
      
      
      
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        
        n=bin(n)[:1:-1]
        len_=len(n)
        n=int(n,2)
        n<<=(32-len_)
        n=bin(n)[2:]
        
        return int(n,2)
        
        
        
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        
        n=bin(n)[:1:-1]
        
        return int(n+'0'*(32-len(n)),2)
