class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        aset=['']
        
        for word in sorted(words):
            if word[:-1] in aset:
                aset.append(word)
                
        return max(sorted(aset), key=lambda x: len(x))
