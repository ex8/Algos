class Chaining:
    """
    Purpose: Hashing with Chaining (handling collisions) using Linked List
    """

    def __init__(self, size=0):
        """
        Purpose: Initialize Separate Chaining Hash Table object
        :param size: number of buckets (best if prime)
        """
        self.size = size                    # Number of buckets
        self.m = 0                          # Number of elements in all buckets
        self.buckets = [None] * self.size   # Buckets

    def hash(self, key):
        """
        Purpose: Hash function using modular hashing
        :param key: string key
        :return:
        """
        return key % self.size

    def find(self, key):
        """
        Purpose: Find value in hash table
        :param key: string key
        :return: value
        """
        bucket = self.hash(key=key)
        if self.buckets[bucket] is None: return
        ll = self.buckets[bucket]
        current = ll.head
        while current:
            if current.key == key:
                return current.data
            current = current.next

    def exists(self, key):
        """
        Purpose: Does key exist in hash table
        :param key: string key
        :return: bool
        """
        bucket = self.hash(key=key)
        if self.buckets[bucket] is None: return False
        ll = self.buckets[bucket]
        current = ll.head
        while current:
            if current.key == key:
                return True
            current = current.next
        return False

    def insert(self, key, value):
        """
        Purpose: Insert new node in hash table
        :param key: key
        :param value: data
        :return:
        """
        bucket = self.hash(key=key)
        if self.buckets[bucket] is None:
            ll = LinkedList()
            ll.add(key=key, value=value)
            self.buckets[bucket] = ll
            self.m += 1
            return
        ll = self.buckets[bucket]
        ll.add(key=key, value=value)
        self.m += 1
        return

    def remove(self, key):
        """
        Purpose: Remove key from hash table
        :param key: string key
        :return:
        """
        bucket = self.hash(key=key)
        if self.buckets[bucket] is None: return
        ll = self.buckets[bucket]
        current = ll.head
        while current:
            if current.key == key:
                ll.delete(key=key)
                self.m -= 1
                return
            current = current.next


class LinkedList:
    """
    Purpose: Simple Singly LL Class
    """

    def __init__(self):
        self.head = None

    def add(self, key, value):
        node = Node(key=key, data=value)
        if self.head is None:
            self.head = node
            return
        current = self.head
        while current:
            if current.next is None:
                current.next = node
                return
            current = current.next

    def delete(self, key):
        if self.head is None: return
        current = self.head
        prev = None
        while current:
            if current.key == key:
                if prev is None:
                    self.head = None
                    return
                prev.next = None
                return
            prev = current
            current = current.next


class Node:
    """
    Purpose: Simple Node Class
    """

    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.next = None
