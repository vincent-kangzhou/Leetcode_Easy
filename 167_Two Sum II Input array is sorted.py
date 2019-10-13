class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_dict={}
        
        for idx, val in enumerate(numbers):
            if (target-val) in num_dict:
                return [num_dict[target-val], idx+1]
            num_dict[val]=idx+1
            
            
            
            
            
class Solution(object):
  def twoSum(self, numbers, target):
      """
      :type numbers: List[int]
      :type target: int
      :rtype: List[int]
      """
      left, right =0, len(numbers)-1
      while left<right:
          if numbers[left]+numbers[right]>target:
              right-=1
          elif numbers[left]+numbers[right]<target:
              left+=1
          else:
              return [left+1, right+1]

      return []
