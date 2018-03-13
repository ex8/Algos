from .node import Node


class DoublyLinkedList:
    def __init__(self, head=None, size=0):
        """
        Purpose: Initialize DLL object
        :param head: pointer to first node in DLL
        :param size: size of DLL
        """
        self.head = head
        self.size = size

    def __len__(self):
        """
        Purpose: Obtain DLL size
        :return size: size of DLL
        """
        return self.size

    def __str__(self):
        """
        Purpose: Print DLL in readable fashion
        :return string:
        """
        current = self.head
        while current:
            print(current.data, "<--> ")
            current = current.next
        print("Size:", self.__len__())

    def empty(self):
        """
        Purpose: Check if DLL is empty
        :return: boolean
        """
        return self.size == 0

    def clear(self):
        """
        Purpose: Clear DLL nodes and size to 0
        :return:
        """
        self.head = None
        self.size = 0

    def push_front(self, data):
        """
        Purpose: Push (add) node to front of DLL
        :param data: new node data
        :return:
        """
        n = Node(data=data)
        if self.head is None:
            self.head = n
            self.size += 1
            return
        old_head = self.head
        self.head = n
        self.head.next = old_head
        old_head.prev = n
        self.size += 1

    def push_back(self, data):
        """
        Purpose: Push (add) node to back of DLL
        :param data: new node data
        :return:
        """
        if self.head is None:
            self.push_front(data=data)
            return
        current = self.head
        n = Node(data=data)
        while current:
            if current.next is None:
                current.next = n
                n.prev = current
                self.size += 1
                return
            current = current.next

    def pop_front(self):
        """
        Purpose: Pop (delete) node from front of DLL
        :return:
        """
        if self.head is None: return
        old_head = self.head
        self.head = old_head.next
        self.head.prev = None
        self.size -= 1

    def pop_back(self):
        """
        Purpose: Pop (delete) node from back of DLL
        :return:
        """
        if self.head is None: return
        current = self.head
        while current:
            if current.next is None:
                current.prev = None
                self.size -= 1
                return
            current = current.next

    def insert(self, index, data):
        """
        Purpose: Insert new node at given index position
        :param index: node index to insert
        :param data: new node data
        :return:
        """
        if index == 0 or self.head is None:
            self.push_front(data=data)
            return
        if index >= self.__len__():
            self.push_back(data=data)
            return
        n = Node(data=data)
        i = 0
        current = self.head
        while current:
            if index == i:
                prev = current.prev
                prev.next = n
                n.prev = prev
                n.next = current
                current.prev = n
                self.size += 1
                return
            i += 1
            current = current.next

    def m_to_last_element(self, m):
        """
        Purpose: Print SLL starting from index 'm' to last node
        :param m: index
        :return:
        """
        if self.head is None: return
        if m > self.__len__(): return
        i = 0
        current = self.head
        while current:
            if i >= m:
                print(current.data, "<--> ")
            i += 1
            current = current.next

    # TODO: fix up reverse LL
    def reverse(self):
        """
        Purpose: Reverse DLL
        :return:
        """
        if self.head is None: return
        if self.head.next is None: return
        current = self.head
        while current:
            prev = current.prev
            current.prev = current.next
            current.next = prev
            current = current.prev
            if prev is not None: self.head = prev.prev
