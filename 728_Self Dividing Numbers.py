class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res=[]
        for num in range(left, right+1):
            A=0
            str_=str(num)
            if '0' in str_:
                continue
            for strr in str_:
                if num%int(strr):
                    A=1
                    break
            if A==0:
                
                res.append(num)
            
        return res
        
        
        
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
                
        
        def isDividingNumber(num):
            if '0' in str(num):
                return False
            return 0 == sum(num % int(i) for i in str(num))
        res=[]
        for num in range(left, right+1):
            if isDividingNumber(num):
                res.append(num)
        return res
                
                
                
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        
        is_self_dividing= lambda num: '0' not in str(num) and all([num%int(digit)==0 for digit in str(num)])
        
        return filter(is_self_dividing, range(left, right+1))
        
        
        
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        
        is_self_dividing= lambda num: '0' not in str(num) and all(num%int(digit)==0 for digit in str(num))
        
        return filter(is_self_dividing, range(left, right+1))
        
        
        
        
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        
        is_self_dividing= lambda num: '0' not in str(num) and not any(num%int(digit)!=0 for digit in str(num))
        # same as def function
        
        return filter(is_self_dividing, range(left, right+1))
