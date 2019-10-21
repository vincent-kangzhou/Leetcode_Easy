
import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        ban = set(banned)
        words = re.findall(r'\w+', paragraph.lower())
        return collections.Counter(w for w in words if w not in ban).most_common(1)[0][0]
    
    
    

import string
import collections
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words=[word.lower().rstrip(string.punctuation) for word in paragraph.split()]
        p=[w for w in words if w not in banned]
        word_dict={w:0 for w in p}
        for word in p:
            word_dict[word]+=1
            
        return max(word_dict, key=lambda k: word_dict[k])
            
