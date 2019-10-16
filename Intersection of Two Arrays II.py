class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=[]
        for i in nums1:
            index=-1
            for j in range(len(nums2)):
                if nums2[j]==i:
                    index=j
                    res.append(i)
                    del nums2[j]
                    break
                
        return res
        
        
        
        
        
        
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=[]
        nums2.sort()
        for k in nums1:
            flag, index=self.binarySearch(nums2, k)
            if flag:
                res.append(k)
                del nums2[index]
        return res
            
            
            
    def binarySearch(self, nums, num):
        left, right=0, len(nums)-1
        
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==num:
                return True, mid
            elif nums[mid]>num:
                right=mid-1
            else:
                left=mid+1
        return False, 0
        
        
        
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=[]
        mapping={}
        for i in nums1:
            mapping[i]=mapping[i]+1 if i in mapping else 1
        
        for j in nums2:
            if j in mapping and mapping[j]>0:
                res.append(j)
                mapping[j]-=1
                
        return res
