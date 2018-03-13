class BinarySearch:
    """
    Purpose: Binary Search on list of numbers
    """

    def __init__(self, numbers=None):
        """
        Purpose: Initialize Binary Search object
        :param numbers: list of numbers (assume sorted)
        """
        self.numbers = numbers or []

    def search(self, n):
        """
        Purpose: Binary Search
        :param n: number to search
        :return: mid
        """
        left = 0
        right = len(self.numbers) - 1
        while left <= right:
            mid = left + int((right - left) / 2)
            if self.numbers[mid] == n:
                return mid
            if self.numbers[mid] < n:
                left = mid + 1
            else:
                right = mid - 1
        return -1
