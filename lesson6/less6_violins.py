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
            self.get_instrument()
            time.sleep(random.randint(1, 5))
            self.put_instrument()
            self.semaphore.release()
            i += 1

    def get_instrument(self):
        self.mutex_violin.acquire()
        self.queue_violin.get('violin')
        print(self.name + ' take violin')
        self.mutex_violin.notify()
        self.mutex_violin.release()
        self.mutex_bow.acquire()
        self.queue_bow.get('bow')
        print(self.name + ' take bow')
        self.mutex_bow.notify()
        self.mutex_bow.release()

    def put_instrument(self):
        self.mutex_violin.acquire()
        self.queue_violin.put('violin')
        print(self.name + ' put violin')
        self.mutex_violin.notify()
        self.mutex_violin.release()
        self.mutex_bow.acquire()
        self.queue_bow.put('bow')
        print(self.name + ' put bow')
        self.mutex_bow.notify()
        self.mutex_bow.release()

maxconnections = 3
pool_sema = BoundedSemaphore(value=maxconnections)

mutex_violin = threading.Condition()
queue_violin = queue.Queue(3)
queue_violin.put('violin')
queue_violin.put('violin')
queue_violin.put('violin')

mutex_bow = threading.Condition()
queue_bow = queue.Queue(3)
queue_bow.put('bow')
queue_bow.put('bow')
queue_bow.put('bow')

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
violinist1.join()
violinist2.join()
violinist3.join()
violinist4.join()
violinist5.join()
violinist6.join()