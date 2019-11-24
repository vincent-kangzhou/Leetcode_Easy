class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        res=[]
        for i in nums1:

            idx=0
            for j in range(nums2.index(i)+1,len(nums2)):
                if i<nums2[j]:
                    idx=j
                    break
                    
            if idx==0:
                res.append(-1)
            else:
                res.append(nums2[idx])
        return res
                
                
                
