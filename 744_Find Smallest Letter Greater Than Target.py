class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        import bisect
        if letters[-1]<=target:
            return letters[0]
#         if letters[0]>=target:
#             return letters[-1]
        
        idx=bisect.bisect_right(letters, target)
        return letters[idx]
        
        
        
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        for letter in letters:
            if letter>target:
                return letter
        return letters[0]
