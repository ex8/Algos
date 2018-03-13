class PriorityQueue:
    """
    Purpose: Priority Queue Class
    """

    def __init__(self, size=0, numbers=None):
        """
        Purpose: Initialize Priority Queue Object
        :param size: size of PQ
        :param numbers: list of numbers
        """
        self.size = size
        self.numbers = numbers or []

    def __len__(self):
        """
        Purpose: Get size of PQ
        :return: size
        """
        return self.size

    def __str__(self):
        """
        Purpose: Print PQ in human read-able fashion
        :return:
        """
        print(self.numbers)
        print("Size: {}".format(self.size))

    def empty(self):
        """
        Purpose: Check if PQ is empty
        :return: bool
        """
        return self.size == 0

    def add(self, n):
        """
        Purpose: Append n to list of numbers
        :param n:
        :return:
        """
        self.numbers.append(n)
        self.size += 1

    def remove_max(self):
        """
        Purpose: Remove max element in PQ list of numbers
        :return: m
        """
        m = max(self.numbers)
        self.numbers.remove(m)
        self.size -= 1
        return m

    def remove_min(self):
        """
        Purpose: Remove min element in PQ list of numbers
        :return: m
        """
        m = min(self.numbers)
        self.numbers.remove(m)
        self.size -= 1
        return m
