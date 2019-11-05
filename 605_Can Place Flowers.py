class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        for i in range (len(flowerbed)):
            if flowerbed[i]==0 and (i==0 or flowerbed[i-1]==0) and (i==len(flowerbed)-1 or flowerbed[i+1]==0):
                flowerbed[i]=1
                n-=1
        return n<=0
        
        
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        for i, num in enumerate(flowerbed):
            if num==1: continue
            if i>0 and flowerbed[i-1]==1: continue
            if i<len(flowerbed)-1 and flowerbed[i+1]==1: continue
            flowerbed[i]=1
            n-=1
        return n<=0




class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if flowerbed[0]==0: flowerbed.insert(0,0)
        if flowerbed[-1]==0: flowerbed.append(0)
        
        cnt=0
        tot=0
            
        for i in flowerbed:
            if i==0: cnt+=1
            else:
                num=max(0,cnt-1)//2
                
                tot+=num
                cnt=0
        tot+=max(0,cnt-1)//2
        return tot>=n
