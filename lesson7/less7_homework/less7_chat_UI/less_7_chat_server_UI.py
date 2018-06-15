import socket
import threading


class ClientHandler(threading.Thread):
    def __init__(self, sock, clients):
        threading.Thread.__init__(self)
        self.sock = sock
        self.clients = clients
        self.daemon = True

    def run(self):
        while True:
            message = self.sock.recv(1024).decode()
            msg_array = message.split(':')
            if message == 'quit_chat':
                for key, value in self.clients.items():
                    if value == self.sock:
                        name = key
                        break
                res = 'client ' + name + ' remove'
                print(res)
                self.clients.pop(name)
                self.sock.shutdown(1)
                break
            elif msg_array[0] == 'name':
                self.clients[msg_array[1]] = self.sock
            elif msg_array[0] == 'list':
                output = ''
                for key in self.clients.keys():
                    output += key + '\n'
                self.sock.send(output.encode())
            elif msg_array[0] == 'broadcast':
                for value in self.clients.values():
                    value.send(msg_array[1].encode())
            elif msg_array[0] in self.clients.keys():
                for key, value in self.clients.items():
                    if value == self.sock:
                        name = key
                output = name + ': ' + msg_array[1]
                self.clients[msg_array[0]].send(output.encode())
            else:
                output = "SERVER: input 'name:', 'user', 'list:' or 'broadcast'"
                self.sock.send(output.encode())
        self.sock.close()



sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('0.0.0.0', 7777)) #указываем что мы сетевое приложение и хотим адрес 5555
sock.listen(5)
clients = {}
while True:
    client_sock, address = sock.accept()
    client_handler = ClientHandler(client_sock, clients)
    client_handler.start()
