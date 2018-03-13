from Trees.binarysearch import BinarySearch
from Trees.bst import BinarySearchTree


def main():
    # b = BinarySearch(numbers=[3, 9, 17, 44, 107])
    # print(b.search(n=44))

    bst = BinarySearchTree()
    bst.insert(data=56)
    bst.insert(data=22)
    bst.insert(data=81)
    bst.insert(data=10)
    bst.insert(data=30)
    bst.insert(data=77)
    bst.insert(data=92)
    bst.insert(data=29)
    bst.in_order()


if __name__ == "__main__":
    main()
