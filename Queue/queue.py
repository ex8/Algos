from .node import Node


class Queue:
    def __init__(self, first=None, last=None, size=0):
        """
        Purpose: Initialize Linked Queue (FIFO) object
        :param first: head of queue
        :param last: tail of queue
        :param size: size of queue
        """
        self.first = first
        self.last = last
        self.size = size

    def __len__(self):
        """
        Purpose: Obtain stack size
        :return:
        """
        return self.size

    def __str__(self):
        """
        Purpose: Print queue in human readable fashion
        :return:
        """
        current = self.first
        while current:
            print(current.data, "--> ")
            current = current.next
        print("Size:", self.__len__())

    def enqueue(self, data):
        """
        Purpose: Add new node to end of queue
        :param data: node data
        :return:
        """
        n = Node(data=data)
        if self.first is None:
            self.first = n
            self.last = self.first
            self.size += 1
            return
        old_last = self.last
        self.last = n
        old_last.next = self.last
        self.size += 1

    def dequeue(self):
        """
        Purpose: Remove and return first node
        :return: removed first node
        """
        if self.first is None: return
        old_first = self.first
        self.first = old_first.next
        self.size -= 1
        return old_first

    def peek(self):
        """
        Purpose; Peek (show) first node in queue
        :return:
        """
        if self.first is None: return
        return self.first.data

    def empty(self):
        """
        Purpose: Check if queue is empty
        :return: bool
        """
        return self.size == 0

    def clear(self):
        """
        Purpose: Clear queue, set first and last to none and size to 0
        :return:
        """
        self.first = None
        self.last = None
        self.size = 0
