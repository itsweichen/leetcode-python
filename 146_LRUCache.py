class LRUCache(object):
    # 5/31/2016
    # get/set: O(n) - mainly involves in update LRU rank
    # 556 ms [19%]

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}
        self.rank = [] # [x1, x2, ..., xn] where xn is the LRU item
        self.num = 0

    def get(self, key):
        """
        :rtype: int
        """
        if key in self.cache:
            self.updateKeyRank(key, True)
            return self.cache[key]
        else:
            return -1

    def updateKeyRank(self, key, existed):
        """
        :key: int
        :if existed: bool
        """
        if existed:
            self.rank.insert(0, self.rank.pop(self.rank.index(key)))
        else:
            self.rank.insert(0, key)

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key in self.cache:
            self.cache[key] = value
            self.updateKeyRank(key, True)
        else:
            if self.num < self.capacity:
                self.cache[key] = value
                self.updateKeyRank(key, False)
                self.num += 1
            else:
                self.cache.pop(self.rank.pop())
                self.cache[key] = value
                self.updateKeyRank(key, False)
