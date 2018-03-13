class LinearProbing:
    """
    Purpose: Hashing with Linear Probing/Open Addressing (handling collisions)
             If key/value is occupied, find next open space in buckets
    """

    def __init__(self, size=0):
        """
        Purpose: Initialize Linear Probing object
        :param size: number of buckets (best if prime)
        """
        self.size = size
        self.m = 0
        self.buckets = [None] * self.size

    def hash(self, key):
        """
        Purpose: Hash function using modular hashing
        :param key: key
        :return:
        """
        return key % self.size

    def insert(self, key, data):
        """
        Purpose: Insert element in hash table
        :param key: key
        :param data: data
        :return:
        """
        bucket = self.hash(key=key)
        if self.buckets[bucket] is None:
            self.buckets[bucket] = data
            self.m += 1
            return
        while bucket:
            bucket += 1
            if bucket >= self.size:
                bucket = 0
            if self.buckets[bucket] is None:
                self.buckets[bucket] = data
                self.m += 1
                return

    def remove(self, key):
        """
        Purpose: Remove element from hash table
        :param key: key
        :return:
        """
        bucket = self.hash(key=key)
        if self.buckets[bucket] is None: return
        self.buckets[bucket] = None

    def exists(self, key):
        """
        Purpose: Check if key exists in hash table
        :param key:
        :return:
        """
        bucket = self.hash(key=key)
        if self.buckets[bucket]: return True
        return False

    def get(self, key):
        """
        Purpose: Get value, given key
        :param key: key
        :return: value
        """
        bucket = self.hash(key=key)
        if self.buckets[bucket] is not None:
            return self.buckets[bucket]
