import threading

class Sum(threading.Thread):
    def __init__(self, begin, end):
        threading.Thread.__init__(self)
        self.begin = begin
        self.end = end
        self.result = 0

    def run(self):
        for i in range(self.begin, self.end):
            self.result += i


first = Sum(1,500000)
second = Sum(500000, 10000001)
first.start()
second.start()
first.join()
second.join()
total = first.result + second.result
print(total)