class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        words_=[]
        for word in words:
            res=[]
            for i in word:
                res.append(order.find(i))
            words_.append(res)
        
        sort_word=[x for x, _ in sorted(zip(words,words_), key=lambda pair: pair[1])]
        
        return sort_word==words
        
        
class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        def p(word):
            res=[]
            for i in word:
                res.append(order.find(i))
            return res
        
        sort_word=sorted(words, key=p)
        
        return sort_word==words
        
        
        
        
class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        dic={val:idx for idx, val in enumerate(order)}
        
        N=len(words)
        for i in range(N-1):        
            pre, after=words[i], words[i+1]
            if pre==after:
                continue
            len_min=min(len(pre), len(after))
            for j in range(len_min):
                if dic[pre[j]]<dic[after[j]]:
                    break
                else:
                    return False
            if len(pre)>len(after) and pre[:len_min]==after:
                return False
        return True
                
                
                
class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        for i in range(len(words)-1):
            for j in range(min(len(words[i]), len(words[i+1]))):
                if order.index(words[i][j]) < order.index(words[i+1][j]):
                    break
                elif order.index(words[i][j]) == order.index(words[i+1][j]):
                    if j == min(len(words[i]), len(words[i+1])) - 1:
                        if len(words[i]) - len(words[i+1]) > 0:
                            return False
                        else:
                            continue
                    continue
                else:
                    return False
        return True
        
        
        alien_dic={}
        for i, c in enumerate(order):
            alien_dic[c] = i

        dic_order = sorted(words, key=lambda x: [alien_dic[c] for c in x])
        return dic_order == words
