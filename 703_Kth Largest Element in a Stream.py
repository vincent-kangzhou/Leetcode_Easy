class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k=k
        self.nums=nums
        

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort(reverse=True)
        return self.nums[self.k-1]
        
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)





class KthLargest:
    import heapq
    def __init__(self, k: int, nums: List[int]):
        self.k=k
        heapq.heapify(nums)
        self.heap=nums
        while len(self.heap)>k:
            heapq.heappop(self.heap)     


    def add(self, val: int) -> int:
        if len(self.heap)<self.k:
            heapq.heappush(self.heap, val)
        else:
            heapq.heappushpop(self.heap, val)
        
        return self.heap[0]



class KthLargest:
    import heapq
    def __init__(self, k: int, nums: List[int]):
        self.k=k
        heapq.heapify(nums)
        self.heap=nums
  


    def add(self, val: int) -> int:

        heapq.heappush(self.heap, val)
        if len(self.heap)>self.k:
            return heapq.nlargest(self.k,self.heap)[-1]
        else:
            return heapq.nlargest(len(self.heap),self.heap)[-1]
