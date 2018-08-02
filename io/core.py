from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import random

class Game(QDialog):
    def __init__(self, QApp):
        super().__init__()
        self.QApp = QApp
    def setupUi(self):
        file = open('root.qss', 'r')
        self.PSQWRootStyle = file.read()
        file.close()
        del file
        self.setStyleSheet(self.PSQWRootStyle)
        self.QGLRoot = QGridLayout()
        self.setLayout(self.QGLRoot)
        self.QLResult = QLabel(self)
        para = random.randrange("吉","大吉","小吉","中吉","中吉","小吉","吉","吉","吉",)
    def startUi(self):
        self.show()

class Root(QMainWindow):
    def __init__(self, QApp):
        super().__init__()
        self.QApp = QApp
    def setupUi(self):
        file = open('root.qss', 'r')
        self.PSQWRootStyle = file.read()
        file.close()
        del file
        self.setStyleSheet(self.PSQWRootStyle)
        self.PLQuestions = [['<b>2/6</b><hr><h1>連絡帳</h1>','ある','いらない'],
                            ['<b>2/6</b><hr><h1>国語の教科書・ノート</h1>','ある','いらない'],
                            ['<b>2/6</b><hr><h1>国語ドリル</h1>','ある','いらない'],
                            ['<b>2/6</b><hr><h1>漢字ドリル</h1>','ある','いらない'],
                            ['<b>2/6</b><hr><h1>算数の教科書・ノート</h1>','ある','いらない'],
                            ['<b>2/6</b><hr><h1>算数ドリル</h1>','ある','いらない'],
                            ['<b>2/6</b><hr><h1>計算ドリル</h1>','ある','いらない'],
                            ['<b>2/6</b><hr><h1>理科の教科書・ノート</h1>','ある','いらない'],
                            ['<b>2/6</b><hr><h1>理科の実験道具</h1>','ある','いらない'],
                            ['<b>2/6</b><hr><h1>社会の教科書・ノート</h1>','ある','いらない'],
                            ['<b>2/6</b><hr><h1>社会の資料集</h1>','ある','いらない'],
                            ['<b>2/6</b><hr><h1>音楽の教科書</h1>','ある','いらない'],
                            ['<b>2/6</b><hr><h1>図工の教科書</h1>','ある','いらない'],
                            ['<b>2/6</b><hr><h1>図工の用意</h1>','ある','いらない'],
                            ['<b>2/6</b><hr><h1>水泳・体操の用意</h1>','ある','いらない'],
                            ['<b>2/6</b><hr><h1>ハンカチとティッシュ</h1>','ある','いらない'],
                            ['<b>2/6</b><hr><h1>上履き</h1>','ある','いらない（火、水、木、金曜日）'],
                            ['<b>2/6</b><hr><h1>給食の用意</h1>','ある','いらない']]
        self.PLQuestionCounter = 0
        self.setWindowTitle('教材チェック')
        self.showMaximized()
        self.QGLRoot = QGridLayout()
        self.QWTDummy = QWidget()
        self.setCentralWidget(self.QWTDummy)
        self.QWTDummy.setLayout(self.QGLRoot)
        self.QLBTool = QLabel(self)
        self.QLBTool.setText('Tool')
        self.QGLRoot.addWidget(self.QLBTool, 0, 0, 0, 2)
        self.QPB0 = QPushButton(self)
        self.QPB0.setText('0')
        self.QPB0.clicked.connect(self.updateUiQPB0)
        self.QGLRoot.addWidget(self.QPB0, 1, 0)
        self.QPB1 = QPushButton(self)
        self.QPB1.setText('ある')
        self.QPB1.clicked.connect(self.updateUiQPB1)
        self.QGLRoot.addWidget(self.QPB1, 1, 1)
    def startUi(self):
        self.show()
        self.updateUi()
    def updateUi(self:)
        self.setText(para)
        # self.QLBTool.setText(self.PLQuestions[self.PLQuestionCounter][0])
        # self.QPB0.setText(self.PLQuestions[self.PLQuestionCounter][1])
        # self.QPB1.setText(self.PLQuestions[self.PLQuestionCounter][2])
        # if self.PLQuestionCounter == len(self.PLQuestions):
            # x = Game(self.QApp)
            # x.setupUi()
            # x.startUi()
    def updateUiQPB0(self):
        if self.PLQuestionCounter != len(self.PLQuestions) - 1:
            self.PLQuestionCounter += 1
        else:
            exit()
        self.updateUi()
    def updateUiQPB1(self):
        if self.PLQuestionCounter != len(self.PLQuestions) - 1:
            self.PLQuestionCounter += 1
        else:
            exit()
        self.updateUi()
QApp = QApplication(sys.argv)

App = Root(QApp)
App.setupUi()
App.startUi()

sys.exit(QApp.exec_())
