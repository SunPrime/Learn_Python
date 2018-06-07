import threading
import queue
import time
import random

class Violinist(threading.Thread):
    def __init__(self, queue, mutex, name):
        threading.Thread.__init__(self)
        self.queue = queue
        self.mutex = mutex
        self.name = name

    def run(self):
        i = 0
        while i < 6:
            viol = self.get_instrument()
            time.sleep(random.randint(1, 5))
            self.put_instrument(viol)
            i += 1

    def get_instrument(self):
        self.mutex.acquire()
        while (self.queue.qsize() == 0):
            self.mutex.wait()
        viol = self.queue.get()
        self.mutex.notify()
        self.mutex.release()
        print(self.name + ' take ' + viol)
        return viol

    def put_instrument(self, viol):
        self.mutex.acquire()
        self.queue.put(viol)
        self.mutex.notify()
        self.mutex.release()
        print(self.name + ' put ' + viol)


queue_violin = queue.Queue(3)
queue_violin.put('violin1')
queue_violin.put('violin2')
queue_violin.put('violin3')

mutex = threading.Condition()

violinist1 = Violinist(queue_violin, mutex, 'Violinist1')
violinist2 = Violinist(queue_violin, mutex, 'Violinist2')
violinist3 = Violinist(queue_violin, mutex, 'Violinist3')
violinist4 = Violinist(queue_violin, mutex, 'Violinist4')
violinist5 = Violinist(queue_violin, mutex, 'Violinist5')
violinist6 = Violinist(queue_violin, mutex, 'Violinist6')

violinist1.start()
violinist2.start()
violinist3.start()
violinist4.start()
violinist5.start()
violinist6.start()
