class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        import collections
        return max(collections.Counter(collections.Counter(arr).values()).values())==1
        
        
        
class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        
        count={}
        for num in arr:
            if num not in count:
                count[num]=1
            else:
                count[num]+=1
        return len(set(count.values()))==len(count)
