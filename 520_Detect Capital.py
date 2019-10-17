class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return word==word.upper() or word==word.lower() or ((word[0].upper()+word.lower()[1:])==word) if len(word)>=2 else word==word.upper() or word==word.lower()
        
