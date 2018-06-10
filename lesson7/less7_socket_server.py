import socket
import threading

class ClientHandler(threading.Thread):
    def __init__(self, sock):
        threading.Thread.__init__(self)
        self.sock = sock

    def run(self):
        message = self.sock.recv(1024).decode()
        message += 'From server'
        self.sock.send(message.encode())
        self.sock.close()


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('0.0.0.0', 5555)) #указываем что мы сетевое приложение и хотим адрес 5555
sock.listen(5)
while True:
    client_sock, address = sock.accept()
    client_handler = ClientHandler(client_sock)
    client_handler.start()