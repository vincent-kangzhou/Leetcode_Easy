class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        nums_set=set(candies)
        if len(nums_set)<=len(candies)//2: return len(nums_set)
        else:
            return len(candies)//2
            
            
            
            
class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        return min(len(set(candies)), len(candies)//2)
