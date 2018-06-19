import socket, select, threading, sys
from PyQt5.QtWidgets import (QMainWindow, QApplication, QDesktopWidget,
                             QTextEdit, QGridLayout, QPushButton, QWidget)


sock = None
class Client_Thread(threading.Thread):
    def __init__(self, chat):
        threading.Thread.__init__(self)
        self.chat = chat

    def run(self):
        global sock
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # идем к ОС и просим порт
        sock.connect(('127.0.0.1', 7777))
        select.select([sock], [sock], [])

        while True:
            message = sock.recv(1024).decode()
            if not message:
                self.chat.centralWidget.get_message('SERVER DISCONNECT')
                break
            else:
                self.chat.centralWidget.get_message(message)
        sock.close()


#chat
class Chat(QMainWindow):
    def __init__(self):
        super().__init__()
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
        self.centralWidget = CentralWidget()
        self.setCentralWidget(self.centralWidget)


class CentralWidget(QWidget):
    def __init__(self):
        super().__init__()
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
        sock.send(text.encode())

    def close(self):
        quit = 'quit_chat'
        sock.send(quit.encode())
        sock.close()
        self.QMainWindow.close()

def main():

    app = QApplication(sys.argv)
    chat = Chat()

    client = Client_Thread(chat)
    client.start()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()