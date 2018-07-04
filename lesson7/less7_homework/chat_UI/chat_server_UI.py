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
            timeout = 30
            self.sock.settimeout(timeout)
            try:
                message = self.sock.recv(1024).decode()
            except socket.timeout:
                print("Time is out, %d seconds have passed" % timeout)
                for key, value in self.clients.items():
                    if value == self.sock:
                        name = key
                res = 'user ' + name + ' not data'
                print(res)
                self.clients.pop(name)
                self.sock.shutdown(1)
                break
            msg_array = message.split(':')
            if message == 'quit_chat':
                for key, value in self.clients.items():
                    if value == self.sock:
                        name = key
                res = 'user ' + name + ' remove'
                print(res)
                self.clients.pop(name)
                self.sock.shutdown(1)
                break
            elif msg_array[0] == 'ping':
                print(str(self.clients.keys()) + ' ping')
            elif msg_array[0] == 'name':
                self.clients[msg_array[1]] = self.sock
            elif msg_array[0] == 'list':
                output = ''
                for key in self.clients.keys():
                    output += key + '\n'
                self.sock.send(output.encode())
            elif msg_array[0] == 'broadcast':
                for value in self.clients.values():
                    try:
                        value.send(msg_array[1].encode())
                    except ConnectionResetError:
                        pass
            elif msg_array[0] in self.clients.keys():
                for key, value in self.clients.items():
                    if value == self.sock:
                        name = key
                output = name + ': ' + msg_array[1]
                self.clients[msg_array[0]].send(output.encode())
            else:
                output = "SERVER: input 'name:', 'list:' or 'broadcast', please"
                self.sock.send(output.encode())
        self.sock.close()


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('0.0.0.0', 7777)) #указываем что мы сетевое приложение и хотим адрес 7777
sock.listen(5)
clients = {}
while True:
    client_sock, address = sock.accept()
    client_handler = ClientHandler(client_sock, clients)
    client_handler.start()
