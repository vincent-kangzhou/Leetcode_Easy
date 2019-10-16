class Solution:
    def checkRecord(self, s: str) -> bool:
        c=collections.Counter(s)
        if c['A']<=1:
            if 'LLL' not in s:
                return True
            else:
                return False
        else:
            return False
            
            
            
class Solution:
    def checkRecord(self, s: str) -> bool:
        return not re.search('A.*A|LLL',s)
