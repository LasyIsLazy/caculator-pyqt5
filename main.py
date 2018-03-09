# coding = utf-8

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QLineEdit
from PyQt5.QtGui import QIcon
from random import randint


class Example(QWidget):

    def __init__(self):

        super().__init__()
        self.initUI()
        # self.num = randint(1, 10)

    def initUI(self):

        self.setGeometry(300, 300, 500, 800)
        self.setWindowTitle('Caculation')
        # self.setWindowIcon(QIcon('xdbcb8.ico'))
        self.resultText = QLineEdit('0', self)
        self.resultText.setGeometry(20, 30, 400, 50)
        self.resultText.setEnabled(False)

        for i in range(3):
            for j in range(3):
                num = i * 3 + j + 1
                btn_num = QPushButton(str(num), self)
                btn_num.setGeometry(50 + j * 50, 150 + i * 50, 70, 30)
                print(num)
                btn_num.clicked.connect(lambda: self.showMessage(num))


        self.show()

    def showMessage(self, num):
        print(':' + str(num))
        self.resultText.setText(str(num))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
