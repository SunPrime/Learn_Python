import multiprocessing

def sum(begin, end, queue):
    result = 0
    for i in range(begin, end):
        result += i
    queue.put(result)

def main():
        queue1 = multiprocessing.Queue()
        queue2 = multiprocessing.Queue()

        p1 = multiprocessing.Process(target=sum, args=(1, 50000, queue1))
        p2 = multiprocessing.Process(target=sum, args=(50000, 100001, queue2))

        p1.start()
        p2.start()
        p1.join()
        p2.join()

        total = queue1.get() + queue2.get()
        print(total)

if __name__ == '__main__':
    main()
