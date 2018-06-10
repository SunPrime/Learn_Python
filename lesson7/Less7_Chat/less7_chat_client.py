import socket
import select
import threading

class Reader(threading.Thread):
    def __init__(self, sock):
        threading.Thread.__init__(self)
        self.sock = sock

    def run(self):
        while True:
            message = self.sock.recv(1024).decode()
            print(message)


class Writer(threading.Thread):
    def __init__(self, sock):
        threading.Thread.__init__(self)
        self.sock = sock

    def run(self):
        while True:
            message = input()
            self.sock.send(message.encode())
            # print(message)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #идем к ОС и просим порт
sock.connect(('127.0.0.1', 7777))
select.select([sock], [sock], [])

reader = Reader(sock)
reader.start()

writer = Writer(sock)
writer.start()

reader.join()