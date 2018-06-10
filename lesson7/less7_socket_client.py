import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #идем к ОС и просим порт
sock.connect(('127.0.0.1', 5555))
message = 'Hello, server! '
sock.send(message.encode())
answer = sock.recv(1024).decode()
print(answer)
sock.close()
