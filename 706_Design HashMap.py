class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashMap=dict()

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """

        self.hashMap[key]=value

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        if key in self.hashMap:
            return self.hashMap[key]
        else:
            return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        if key in self.hashMap:
            del self.hashMap[key]
        else:
            pass


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)




class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashMap=[-1]*1000000

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """

        self.hashMap[key]=value

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """

        return self.hashMap[key]


    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
 
        self.hashMap[key]=-1



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)






class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.buckets = 1000
        self.itemsPerBuckect = 1001
        self.hashmap = [[] for _ in range(self.buckets)]

    def hash(self, key):
        return key % self.buckets

    def pos(self, key):
        return key // self.buckets

    def put(self, key, value):
        """
        value will always be positive.
        :type key: int
        :type value: int
        :rtype: void
        """
        hashkey = self.hash(key)
        if not self.hashmap[hashkey]:
            self.hashmap[hashkey] = [None] * self.itemsPerBuckect
        self.hashmap[hashkey][self.pos(key)] = value

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        hashkey = self.hash(key)
        if (not self.hashmap[hashkey]) or self.hashmap[hashkey][self.pos(key)] == None:
            return -1
        else:
            return self.hashmap[hashkey][self.pos(key)]

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """
        hashkey = self.hash(key)
        if self.hashmap[hashkey]:
            self.hashmap[hashkey][self.pos(key)] = None


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)





class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashmap=[-1]*1000001
        


    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        self.hashmap[key]=value
        
    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        return self.hashmap[key]
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        self.hashmap[key]=-1



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
