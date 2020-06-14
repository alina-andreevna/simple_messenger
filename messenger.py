from PyQt5 import QtCore, QtGui, QtWidgets
import client_ui
import requests
import datetime


class MessengerWindow(QtWidgets.QMainWindow, client_ui.Ui_Messenger):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.sendButton.pressed.connect(self.sendMessage)
        self.last_message_time = 0
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.getUpdates)
        self.timer.start(1000)

    def sendMessage(self):
        username = self.usernameEdit.text()
        password = self.passwordEdit.text()
        text = self.userMessage.toPlainText()

        if not username:
            self.addText('ERROR: username is empty')
            return
        if not password:
            self.addText('ERROR: password is empty')
            return
        if not text:
            self.addText('ERROR: text is empty')
            return

        response = requests.post('http://127.0.0.1:5000/send',
                                 json={'username': username, 'password': password, 'text': text})

        if not response.json()['ok']:
            self.addText('ERROR: Access denied')
            return

        self.userMessage.clear()
        self.userMessage.repaint()

    def addText(self, text):
        self.allMessages.append(text)
        self.allMessages.repaint()

    def getUpdates(self):
        response = requests.get('http://127.0.0.1:5000/history',
                                params={'after': self.last_message_time})
        data = response.json()
        for message in data['messages']:
            beauty_time = datetime.datetime.fromtimestamp(message['time'])
            beauty_time = beauty_time.strftime('%Y/%m/%d %H:%M:%S')
            self.addText(beauty_time + '\n' + message['username'] + ': ' + message['text'])
            self.addText('')
            self.last_message_time = message['time']


app = QtWidgets.QApplication([])
window = MessengerWindow()
window.show()
app.exec_()
