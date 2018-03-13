class BinarySearchTree:
    """
    Purpose: Binary Search Tree (Ordered Tree) Class
             This implementation is done with an iterative approach
    """

    def __init__(self, root=None, size=0):
        """
        Purpose: Initialize Binary Search Tree Object
        :param root: BST root node
        :param size: total number of nodes in BST
        """
        self.root = root
        self.size = size

    def __len__(self):
        """
        Purpose: Return number of nodes in BST
        :return: size
        """
        return self.size

    def __str__(self):
        """
        Purpose: Print all nodes in order
        :return: in_order traversal
        """
        return self.in_order()

    def insert(self, data):
        """
        Purpose: Insert node in BST
        :param data: node data
        :return:
        """
        node = Node(data=data)
        if self.root is None:
            self.root = node
            self.size += 1
            return
        current = self.root
        while current:
            parent = current
            if data < current.data:
                current = current.left
                if current is None:
                    parent.left = node
                    self.size += 1
                    return
            else:
                current = current.right
                if current is None:
                    parent.right = node
                    self.size += 1
                    return

    # TODO: Finish del method
    def delete(self, data):
        """
        Purpose: Delete node from BST
        :param data: node data
        :return:
        """
        if self.root is None: return
        current = self.root
        parent = None
        while current:
            if current.data == data:
                # Node has 0 children -> is leaf node
                if current.left is None and current.right is None:
                    if parent.left.data == current.data:
                        parent.left = None
                        self.size -= 1
                        return
                    else:
                        parent.right = None
                        self.size -= 1
                        return
                # Node has 1 right child
                elif current.left is None:
                    if parent.left.data == current.data:
                        parent.left = current.right
                        self.size -= 1
                        return
                    else:
                        parent.right = current.right
                        self.size -= 1
                        return
                # Node has 1 left child
                elif current.right is None:
                    if parent.left.data == current.data:
                        parent.left = current.left
                        self.size -= 1
                        return
                    else:
                        parent.right = current.left
                        self.size -= 1
                        return
                # Node has 2 children
                else:
                    pass
            elif data < current.data:
                parent = current
                current = current.left
            else:
                parent = current
                current = current.right

    def find(self, data):
        """
        Purpose: Find node in BST given data
        :param data: node data
        :return: node
        """
        if self.root is None: return
        current = self.root
        while current:
            if data == current.data:
                return current
            if data < current.data:
                current = current.left
            else:
                current = current.right

    def pre_order(self):
        """
        Purpose: Pre-order BST traversal (N-L-R)
        :return:
        """
        if self.root is None: return
        stack = [self.root]
        while len(stack) != 0:
            current = stack.pop()
            print(current.data)
            if current.right is not None:
                stack.append(current.right)
            if current.left is not None:
                stack.append(current.left)

    def in_order(self):
        """
        Purpose: In-order BST traversal (L-N-R)
        :return:
        """
        if self.root is None: return
        stack = []
        current = self.root
        while current or len(stack) != 0:
            if current is not None:
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                print(current.data)
                current = current.right

    def post_order(self):
        """
        Purpose: Post-order BST traversal (L-R-N)
        :return:
        """
        if self.root is None: return
        stack1 = [self.root]
        stack2 = []
        while len(stack1) > 0:
            node = stack1.pop()
            stack2.append(node)
            if node.left is not None:
                stack1.append(node.left)
            if node.right is not None:
                stack1.append(node.right)
        while len(stack2) > 0:
            node = stack2.pop()
            print(node.data)

    def height(self):
        """
        Purpose: Get height of BST
        :return:
        """
        if self.root is None: return 0
        height = 0
        queue = [self.root]
        while True:
            node_count = len(queue)
            if node_count == 0:
                return height
            height += 1
            while node_count > 0:
                node = queue[0]
                queue.pop(0)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
                node_count -= 1

    def is_bst(self):
        """
        Purpose: Check if current Tree is a BST
        :return:
        """
        if self.root is None: return
        pass

    def is_balanced(self):
        """
        Purpose: Check if BST is balanced
        :return:
        """
        if self.root is None: return
        pass

    def get_successor(self, data):
        """
        Purpose: Get next highest-value (parent node) in BST given value
        :param node:
        :return:
        """
        if self.root is None: return
        pass

    def min(self):
        """
        Purpose: Get the minimum node found in the BST
        :return:
        """
        if self.root is None: return
        current = self.root
        while current.left is not None:
            current = current.left
        return current

    def max(self):
        """
        Purpose: Get the maximum node found in the BSTs
        :return:
        """
        if self.root is None: return
        current = self.root
        while current.right is not None:
            current = current.right
        return current

    def clear(self):
        """
        Purpose: Clear BST
        :return:
        """
        self.root = None
        self.size = 0


class Node:
    """
    Simple Node Class
    """
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
