from LinkedList.singly import SinglyLinkedList
from LinkedList.doubly import DoublyLinkedList


def main():
    # sll = SinglyLinkedList()
    # sll.push_front(data=10)
    # sll.push_front(data=5)
    # sll.push_back(data=15)
    # sll.push_back(data=20)
    # sll.insert(index=2, data=17)
    # sll.reverse()
    # sll.reverse()
    # sll.__str__()

    dll = DoublyLinkedList()
    dll.push_front(data=10)
    dll.push_front(data=5)
    dll.push_back(data=15)
    dll.push_back(data=15)
    dll.insert(index=2, data=17)
    dll.reverse()
    dll.reverse()
    dll.__str__()


if __name__ == "__main__":
    main()
