# coding = utf-8

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QLineEdit
from PyQt5.QtGui import QIcon


class Calculator(QWidget):

    def __init__(self):

        super().__init__()
        self.initUI()
        self.status = 0  # 0: cleared; 1: calculating; 2: calculated.
        self.currentOperator = ''
        self.result = 0

    def initUI(self):

        self.setGeometry(300, 300, 500, 800)
        self.setWindowTitle('Calculator')
        # self.setWindowIcon(QIcon('xdbcb8.ico'))
        self.text_shown = QLineEdit('0', self)  # show expression and result.
        self.text_shown.setGeometry(20, 30, 400, 50)
        self.text_shown.setEnabled(False)

        for i in range(3):
            for j in range(3):
                num = i * 3 + j + 1
                btn_num = QPushButton(str(num), self)
                btn_num.setGeometry(50 + j * 100, 150 + i * 50, 70, 30)
                btn_num.clicked.connect(self.show_message)

        btn_operator = QPushButton('0', self)
        btn_operator.setGeometry(150, 300, 70, 30)
        btn_operator.clicked.connect(self.show_message)

        btn_operator = QPushButton('+', self)
        btn_operator.setGeometry(400, 150, 70, 30)
        btn_operator.clicked.connect(self.show_message)

        btn_operator = QPushButton('-', self)
        btn_operator.setGeometry(400, 200, 70, 30)
        btn_operator.clicked.connect(self.show_message)

        btn_operator = QPushButton('*', self)
        btn_operator.setGeometry(400, 250, 70, 30)
        btn_operator.clicked.connect(self.show_message)

        btn_operator = QPushButton('/', self)
        btn_operator.setGeometry(400, 300, 70, 30)
        btn_operator.clicked.connect(self.show_message)

        btn_operator = QPushButton('=', self)
        btn_operator.setGeometry(400, 350, 70, 30)
        btn_operator.clicked.connect(self.show_message)

        btn_operator = QPushButton('clear', self)
        btn_operator.setGeometry(400, 400, 70, 30)
        btn_operator.clicked.connect(self.show_message)

        self.show()

    def show_message(self):

        next_input = self.sender().text()  # button value.
        current_result_text = self.text_shown.text()
        operators = ('+', '-', '*', '/', '=')
        operators1 = ('+', '-', '*', '/')
        operators2 = ('=')

        # print(next_input in operators2)

        def show():
            self.text_shown.setText(current_result_text + str(next_input))
            self.status = 1
            self.currentOperator = next_input

        def result_operation_show():
            print(str(self.result) + str(next_input))
            self.text_shown.setText(str(self.result) + str(next_input))
            self.status = 1
            self.currentOperator = next_input

        def clear_show():
            self.text_shown.setText(str(next_input))
            self.status = 1
            self.currentOperator = ''

        def eval_show():
            result = eval(current_result_text)
            self.result = result
            self.text_shown.setText(current_result_text + '=' + str(result))
            self.status = 2
            self.currentOperator = '='

        def clear():
            self.text_shown.setText('0')
            self.status = 0
            self.currentOperator = ''

        if next_input == 'clear':
            clear()
        else:
            if self.currentOperator in operators:
                if self.currentOperator in operators1:
                    if next_input in operators:
                        return
                    else:
                        show()
                else:  # self.currentOperator in operators2
                    if next_input in operators:
                        if next_input in operators2:
                            return
                        else:  # next_input in operators1
                            result_operation_show()
                    else:
                        clear_show()
            else:
                if next_input in operators:
                    if next_input in operators1:
                        show()
                    else:  # next_input in operators2
                        eval_show()
                else:
                    if self.status == 0:
                        clear_show()
                    else:
                        show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Calculator()
    sys.exit(app.exec_())
