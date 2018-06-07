import threading
import queue

class Producer(threading.Thread):
    def __init__(self, queue, mutex, name):
        threading.Thread.__init__(self)
        self.queue = queue
        self.mutex = mutex
        self.name = name

    def run(self):
        while True:
            self.mutex.acquire()
            while (self.queue.qsize() > 4):
                self.mutex.wait()
            self.queue.put('box')
            self.mutex.notify()
            self.mutex.release()
            print('He thread ' + self.name + ' put the element')

class Consumer(threading.Thread):
    def __init__(self, queue, mutex, name):
        threading.Thread.__init__(self)
        self.queue = queue
        self.mutex = mutex
        self.name = name

    def run(self):
        while True:
            self.mutex.acquire()
            while (self.queue.qsize() == 0):
                self.mutex.wait()
            self.queue.get()
            self.mutex.notify()
            self.mutex.release()
            print('He thread ' + self.name + ' get the element')

queue = queue.Queue()
mutex = threading.Condition()
p1 = Producer(queue, mutex, 'P1')
p2 = Producer(queue, mutex, 'P2')
c1 = Consumer(queue, mutex, 'C1')
c2 = Consumer(queue, mutex, 'C2')
c3 = Consumer(queue, mutex, 'C3')

p1.start()
p2.start()
c1.start()
c2.start()
c3.start()
p1.join()