class RecentCounter(object):

    def __init__(self):
        self.nums=[]

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.nums.append(t)
        total_re=len(self.nums)
        prev=bisect.bisect_left(self.nums, t-3000)
        return total_re-prev


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)



class RecentCounter(object):

    def __init__(self):
        self.que=collections.deque()

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        while self.que and self.que[0]<t-3000:
            self.que.popleft()
            
        self.que.append(t)
        return len(self.que)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
