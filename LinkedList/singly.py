from LinkedList.node import Node


class SinglyLinkedList:
    def __init__(self, head=None, size=0):
        """
        Purpose: Initialize SLL object
        :param head: pointer to first node in SLL
        :param size: size of SLL
        """
        self.head = head
        self.size = size

    def __len__(self):
        """
        Purpose: Obtain SLL size
        :return size: size of SLL
        """
        return self.size

    def __str__(self):
        """
        Purpose: Print SLL in readable fashion
        :return string:
        """
        current = self.head
        while current:
            print(current.data, "--> ")
            current = current.next
        print("Size:", self.__len__())

    def empty(self):
        """
        Purpose: Check if SLL is empty
        :return: boolean
        """
        return self.size == 0

    def clear(self):
        """
        Purpose: Clear SLL nodes and size to 0
        :return:
        """
        self.head = None
        self.size = 0

    def push_front(self, data):
        """
        Purpose: Push (add) node to front of SLL
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
        n.next = old_head
        self.size += 1

    def push_back(self, data):
        """
        Purpose: Push (add) node to back of SLL
        :param data: new node data
        :return:
        """
        if self.head is None:
            self.push_front(data=data)
            return
        n = Node(data=data)
        current = self.head
        while current:
            if current.next is None:
                current.next = n
                self.size += 1
                return
            current = current.next

    def pop_front(self):
        """
        Purpose: Pop (delete) node from front of SLL
        :return:
        """
        if self.head is None: return
        self.head = self.head.next
        self.size -= 1

    def pop_back(self):
        """
        Purpose: Pop (delete) node from back of SLL
        :return:
        """
        if self.head is None: return
        current = self.head
        prev = self.head
        while current:
            if current.next is None:
                prev.next = None
                self.size -= 1
                return
            prev = current
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
        prev = self.head
        while current:
            if index == i:
                prev.next = n
                n.next = current
                self.size += 1
                return
            i += 1
            prev = current
            current = current.next

    def m_to_last_element(self, m):
        """
        Purpose: Print SLL starting from index 'm' to last node
        :param m: index
        :return:
        """
        if self.head is None: return
        if m > self.__len__():
            self.__str__()
            return
        i = 0
        current = self.head
        while current:
            if i >= m:
                print(current.data, "--> ")
            i += 1
            current = current.next

    def reverse(self):
        """
        Purpose: Reverse SLL
        :return:
        """
        if self.head is None: return
        if self.head.next is None: return
        current = self.head
        prev = None
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
