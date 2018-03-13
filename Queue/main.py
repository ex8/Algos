from Queue.queue import Queue


def main():
    q = Queue()
    q.enqueue(data=5)
    q.enqueue(data=10)
    q.enqueue(data=15)
    q.dequeue()
    q.dequeue()
    q.__str__()

if __name__ == "__main__":
    main()