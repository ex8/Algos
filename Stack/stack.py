from Stack.node import Node


class Stack:
    def __init__(self, top=None, size=0):
        """
        Purpose: Initialize Linked Stack (LIFO) Object
        :param top: top node (last in)
        :param size: size of stack
        """
        self.top = top
        self.size = size

    def __len__(self):
        """
        Purpose: Obtain stack size
        :return:
        """
        return self.size

    def __str__(self):
        """
        Purpose: Print stack in human readable fashion
        :return:
        """
        current = self.top
        while current:
            print(current.data, "--> ")
            current = current.next
        print("Size:", self.__len__())

    def push(self, data):
        """
        Purpose: Push (add) node to top of the stack
        :param data: new node data
        :return:
        """
        n = Node(data=data)
        if self.top is None:
            self.top = n
            self.size += 1
            return
        old_top = self.top
        self.top = n
        self.top.next = old_top
        self.size += 1

    def pop(self):
        """
        Purpose: Pop (remove) node at top of stack
        :return: removed top node
        """
        if self.top is None: return
        old_top = self.top
        self.top = old_top.next
        self.size -= 1
        return old_top

    def peek(self):
        """
        Purpose: Peek (view) node at top of stack
        :return: top node
        """
        if self.top is None: return
        return self.top

    def clear(self):
        """
        Purpose: Clear stack of nodes and size to 0
        :return:
        """
        self.top = None
        self.size = 0

    def empty(self):
        """
        Purpose: Check if stack is empty
        :return: bool
        """
        return self.size == 0
