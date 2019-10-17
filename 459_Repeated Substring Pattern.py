class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        d = 1
        while d * d <= n:
            if n % d == 0:
                for m in {d, n//d}:
                    if m > 1 and m * s[:n//m] == s:
                        return True
            d += 1
        return False






class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if not s:
            return False
        ss=(s+s)[1:-1]
        
        return ss.find(s) !=-1
