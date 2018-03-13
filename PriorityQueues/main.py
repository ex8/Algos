from PriorityQueues.priorityq import PriorityQueue


def main():
    pq = PriorityQueue()
    pq.add(n=5)
    pq.add(n=15)
    pq.add(n=10)
    pq.add(n=9)
    pq.__str__()
    print(pq.remove_max())
    pq.__str__()
    print(pq.remove_max())
    pq.__str__()
    print(pq.remove_max())
    pq.__str__()


if __name__ == "__main__":
    main()