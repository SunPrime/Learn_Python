import threading
import random
import time
import queue
from threading import BoundedSemaphore

import time
import random

class Violinist(threading.Thread):
    def __init__(self, semaphore, queue_violin, queue_bow, mutex_violin, mutex_bow, name):
        threading.Thread.__init__(self)
        self.semaphore = semaphore
        self.queue_violin = queue_violin
        self.queue_bow = queue_bow
        self.mutex_violin = mutex_violin
        self.mutex_bow = mutex_bow
        self.name = name

    def run(self):
        i = 0
        while i < 6:
            self.semaphore.acquire()
            viol, bow = self.get_instrument()
            time.sleep(random.randint(1, 5))
            self.put_instrument(viol, bow)
            self.semaphore.release()
            time.sleep(2)
            i += 1

    def get_instrument(self):
        self.mutex_violin.acquire()
        while (self.queue_violin.qsize() == 0):
            self.mutex_violin.wait()
        viol = self.queue_violin.get()
        print(self.name + ' take ' + viol)
        self.mutex_violin.notify()
        self.mutex_violin.release()

        self.mutex_bow.acquire()
        while (self.queue_bow.qsize() == 0):
            self.mutex_bow.wait()
        bow = self.queue_bow.get()
        print(self.name + ' take ' + bow)
        self.mutex_bow.notify()
        self.mutex_bow.release()

        return viol, bow

    def put_instrument(self, viol, bow):
        self.mutex_violin.acquire()
        self.queue_violin.put(viol)
        print(self.name + ' put ' + viol)
        self.mutex_violin.notify()
        self.mutex_violin.release()
        self.mutex_bow.acquire()
        self.queue_bow.put(bow)
        print(self.name + ' put ' + bow)
        self.mutex_bow.notify()
        self.mutex_bow.release()

maxconnections = 3
pool_sema = BoundedSemaphore(value=maxconnections)

mutex_violin = threading.Condition()
queue_violin = queue.Queue(3)
queue_violin.put('violin1')
queue_violin.put('violin2')
queue_violin.put('violin3')

mutex_bow = threading.Condition()
queue_bow = queue.Queue(3)
queue_bow.put('bow1')
queue_bow.put('bow2')
queue_bow.put('bow3')

mutex = threading.Condition()

violinist1 = Violinist(pool_sema, queue_violin, queue_bow, mutex_violin, mutex_bow, 'Violinist1')
violinist2 = Violinist(pool_sema, queue_violin, queue_bow, mutex_violin, mutex_bow, 'Violinist2')
violinist3 = Violinist(pool_sema, queue_violin, queue_bow, mutex_violin, mutex_bow, 'Violinist3')
violinist4 = Violinist(pool_sema, queue_violin, queue_bow, mutex_violin, mutex_bow, 'Violinist4')
violinist5 = Violinist(pool_sema, queue_violin, queue_bow, mutex_violin, mutex_bow, 'Violinist5')
violinist6 = Violinist(pool_sema, queue_violin, queue_bow, mutex_violin, mutex_bow, 'Violinist6')

violinist1.start()
violinist2.start()
violinist3.start()
violinist4.start()
violinist5.start()
violinist6.start()