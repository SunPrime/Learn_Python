import socket, select, threading, sys
import time
from PyQt5.QtWidgets import (QMainWindow, QApplication, QDesktopWidget,
                             QTextEdit, QGridLayout, QPushButton, QWidget)



class Client_Thread(threading.Thread):
    def __init__(self, sock, chat):
        threading.Thread.__init__(self)
        self.sock = sock
        self.chat = chat

    def run(self):
        while True:
            message = self.sock.recv(1024).decode()
            if not message:
                self.chat.centralWidget.get_message('SERVER DISCONNECT')
                break
            else:
                self.chat.centralWidget.get_message(message)
        self.sock.close()

class Ping_Thread(threading.Thread):
    def __init__(self, sock):
        threading.Thread.__init__(self)
        self.sock = sock
        self.daemon = True

    def run(self):
        while True:
            time.sleep(25)
            self.sock.send('ping'.encode())


#chat
class Chat(QMainWindow):
    def __init__(self, sock):
        super().__init__()
        self.sock = sock
        self.centralWidget=''
        self.initUI()

    def initUI(self):
        self.populateUI()
        self.resize(400, 400)
        self.center()
        self.setWindowTitle('Chat')
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def populateUI(self):
        self.centralWidget = CentralWidget(self.sock)
        self.setCentralWidget(self.centralWidget)


class CentralWidget(QWidget):
    def __init__(self, sock):
        super().__init__()
        self.sock = sock
        self.initUI()

    def initUI(self):
        self.ribbon = QTextEdit()
        self.ribbon.setReadOnly(True)
        self.chat = QTextEdit()
        self.chat.createStandardContextMenu()
        self.sendBtn = QPushButton('&Send')
        self.sendBtn.clicked.connect(self.send_message)
        self.quitBth = QPushButton('&Quit')
        self.quitBth.clicked.connect(self.close)

        grid = QGridLayout()
        grid.setSpacing(2)
        grid.addWidget(self.ribbon, 0, 0, 1, 3)
        grid.addWidget(self.chat, 1, 0, 1, 3)
        grid.addWidget(self.sendBtn, 2, 1)
        grid.addWidget(self.quitBth, 2, 2)

        self.setLayout(grid)

    def get_message(self, message):
        self.ribbon.append(message)

    def send_message(self):
        text = self.chat.toPlainText()
        self.chat.clear()
        text_formatted = '{:>80}'.format(text)
        self.ribbon.append(text_formatted)
        self.sock.send(text.encode())

    def close(self):
        quit = 'quit_chat'
        self.sock.send(quit.encode())
        self.sock.close()
        self.QMainWindow.close()

def main():

    app = QApplication(sys.argv)

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # идем к ОС и просим порт
    sock.connect(('127.0.0.1', 7777))
    select.select([sock], [sock], [])

    chat = Chat(sock)
    client = Client_Thread(sock, chat)
    client.start()

    ping = Ping_Thread(sock)
    ping.start()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()