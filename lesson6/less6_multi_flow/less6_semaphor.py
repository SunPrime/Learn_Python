import threading

class StateException(Exception):
    pass

class Semaphore:
    def __init__(self, value):
        self.value = value
        self.mutex = threading.Condition()
        self.threads = []

    def acquire(self):
        th = threading.current_thread()
        if th in self.threads:
            raise StateException
        self.mutex.acquire()
        self.threads.append(th)
        while self.value == 0:
            self.mutex.wait()
        self.value -= 1
        self.mutex.release()

    def release(self):
        th = threading.current_thread()
        if not th in self.threads:
            raise StateException()
        self.mutex.acquire()
        self.threads.remove(th)
        self.value += 1
        self.mutex.notify()
        self.mutex.release()

class TestThread(threading.Thread):
    def __init__(self, s, name):
        threading.Thread.__init__(self)
        self.s = s
        self.name = name

    def run(self):
        while True:
            self.s.acquire()
            print('The thread ' + self.name + ' required the semaphor')
            self.s.release()

s = Semaphore(2)
t1 = TestThread(s, 'T1')
t2 = TestThread(s, 'T2')
t3 = TestThread(s, 'T3')
t1.start()
t2.start()
t3.start()
t1.join()