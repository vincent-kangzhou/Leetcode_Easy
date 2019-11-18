class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        ans=[]
        hexs='0123456789abcdef'
        
        if num<0: num+=0x100000000
        # 1<<32
            
        while num:
            ans.append(hexs[num%16])
            num/=16
        return ''.join(ans[::-1]) if ans else '0'
        
        
class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        ans=[]
        hexs='0123456789abcdef'
        if num<0: num=(-num^0xFFFFFFFF)+1
            
        while num:
            ans.append(hexs[num%16])
            num/=16
            
        return ''.join(ans[::-1]) if ans else '0'
        
        
class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        ans=[]
        hexs='0123456789abcdef'
        while num:
            value=num&0xf
            ans.append(hexs[value])
            
            num=num>>4 if num>0 else (num%0x100000000)>>4
            
        return ''.join(ans[::-1]) if ans else '0'
