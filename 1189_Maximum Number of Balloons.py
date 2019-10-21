class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        import collections
        num_dict=collections.Counter(text)
        one_word=min(num_dict['b'], num_dict['a'],num_dict['n'], num_dict['l']//2, num_dict['o']//2)
        
        return one_word
        
        
        
class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        target='balloon'
        num_dict=dict.fromkeys(target,0)
        for ch in text:
            if ch in target:
                num_dict[ch]+=1
                
        num_dict['l']=num_dict['l']//2
        num_dict['o']=num_dict['o']//2
        return min(num_dict.values())
