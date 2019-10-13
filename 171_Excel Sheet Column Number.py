class Solution:
    def titleToNumber(self, s: str) -> int:
        s=s.upper()
        letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        mapping={}
        for i in range(1,len(letters)+1):
            mapping[letters[i-1]]=i
        col=0
        for i in s:
            col=26*col+mapping[i]
        return col
