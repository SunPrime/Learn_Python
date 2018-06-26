import multiprocessing
import queue
import time


def sum(begin, end, dict_res):
    result = 0
    for i in range(begin, end):
        result += i
    dict_res['result'] = result


def calculate(queue, mutex):
    while True:
        mutex.acquire()
        while queue.qsize() == 0:
            mutex.wait()
        tuple_queue = queue.get()
        mutex.release()
        globals()[tuple_queue[0]](tuple_queue[1], tuple_queue[2], tuple_queue[3])


class ProcessingPool():
    def __init__(self):
        self.pool = queue.Queue()
        self.queue = multiprocessing.Queue()
        self.mutex = multiprocessing.Condition()

    def create(self):
        for i in range(4):
            proc = multiprocessing.Process(target=calculate, args=(self.queue, self.mutex, ))
            proc.start()
            self.pool.put(proc)

    def submit(self, method_name, begin, end, dict_res):
        self.mutex.acquire()
        self.queue.put((method_name, begin, end, dict_res))
        self.mutex.notify()
        self.mutex.release()


def main():
    proc_pool = ProcessingPool()
    proc_pool.create()
    my_queue = multiprocessing.Manager().dict()

    proc_pool.submit('sum', 1, 101, my_queue)
    time.sleep(2)
    print(my_queue['result'])


if __name__ == "__main__":
    main()