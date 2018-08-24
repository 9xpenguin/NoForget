from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import random

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
        self.PLQuestions = [['<b>1/6</b><hr><h1>連絡帳</h1>','ある','いらない'],
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
    def updateUi(self):
        self.QLBTool.setText(self.PLQuestions[self.PLQuestionCounter][0])
        self.QPB0.setText(self.PLQuestions[self.PLQuestionCounter][1])
        self.QPB1.setText(self.PLQuestions[self.PLQuestionCounter][2])
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
class Game(QMainWindow):
    def __init__(self, QApp):
        super().__init__()
        self.QApp = QApp
    def setupUi(self):
        file = open('root.qss', 'r')
        self.PSQWRootStyle = file.read()
        file.close()
        del file
        self.setStyleSheet(self.PSQWRootStyle)
        self.setWindowTitle('ゲーム')
        self.showMaximized()
        self.QGLRoot = QGridLayout()
        self.QWTDummy = QWidget()
        self.setCentralWidget(self.QWTDummy)
        self.QWTDummy.setLayout(self.QGLRoot)
        self.QLBGuide = QLabel(self)
        self.QLBGuide.setObjectName('Guide')
        self.QLBGuide.setText('じゃんけん')
        self.QGLRoot.addWidget(self.QLBGuide, 1, 0)
        self.QPBRock = QPushButton(self)
        self.QPBRock.setObjectName('Rock')
        self.QPBRock.setText('グー')
        self.QPBRock.clicked.connect(self.updateUiClicked)
        self.QGLRoot.addWidget(self.QPBRock, 2, 0)
        self.QPBScissor = QPushButton(self)
        self.QPBScissor.setObjectName('Scissor')
        self.QPBScissor.setText('チョキ')
        self.QPBScissor.clicked.connect(self.updateUiClicked)
        self.QGLRoot.addWidget(self.QPBScissor, 2, 1)
        self.QPBPaper = QPushButton(self)
        self.QPBPaper.setObjectName('Paper')
        self.QPBPaper.setText('パー')
        self.QPBPaper.clicked.connect(self.updateUiClicked)
        self.QGLRoot.addWidget(self.QPBPaper, 2, 2)
    def startUi(self):
        self.show()
    def updateUiClicked(self):
        if random.randint(0, 1) == 0:
            self.QLBGuide('勝ち')
        else:
            self.QLBGuide('負け')
QApp = QApplication(sys.argv)

App = Root(QApp)
App.setupUi()
App.startUi()
Game = Game(QApp)
Game.setupUi()
Game.startUi()

sys.exit(QApp.exec_())
me
