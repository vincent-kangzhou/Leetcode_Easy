class Solution:
    def isPerfectSquare(self, num: int) -> bool: 
        if num==1 or num==4:
            return True
        if num==2 or num==3:
            return False
        p,q=1,num
        while q-p>1:
            mid=(p+q)//2
            if mid**2>num:
                q=mid
            elif mid**2<num:
                p=mid
            else:
                return True
        return False
        
        
        
        
        
class Solution:
    def isPerfectSquare(self, num: int) -> bool: 
        left, right = 0, num
        while left <= right:
            mid = (left+right) // 2             
            if mid ** 2 == num:
                return True            
            elif mid ** 2 < num:
                left = mid + 1
            else:
                right = mid -1
        return False
