# coding = utf-8

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QLineEdit
from PyQt5.QtGui import QIcon


class Calculator(QWidget):

    def __init__(self):

        super().__init__()
        self.status = 0  # 0: cleared; 1: calculating; 2: calculated.
        self.currentInput = ''
        self.result = 0
        self.text_shown = None
        self.message_show = None
        self.initUI()

    def initUI(self):

        self.setGeometry(300, 300, 500, 800)
        self.setWindowTitle('Calculator')
        # self.setWindowIcon(QIcon('xdbcb8.ico'))

        self.text_shown = QLineEdit('0', self)  # show expression and result.
        self.text_shown.setGeometry(20, 30, 400, 50)
        self.text_shown.setEnabled(False)

        self.message_show = QLineEdit('', self)  # show message when input is wrong.
        self.message_show.setGeometry(50, 350, 270, 40)
        self.message_show.setEnabled(False)

        for i in range(3):
            for j in range(3):
                num = i * 3 + j + 1
                btn_num = QPushButton(str(num), self)
                btn_num.setGeometry(50 + j * 100, 150 + i * 50, 70, 30)
                btn_num.clicked.connect(self.show_message)

        btn_operator = QPushButton('.', self)
        btn_operator.setGeometry(50, 300, 70, 30)
        btn_operator.clicked.connect(self.show_message)

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
        btn_operator.setGeometry(250, 300, 70, 30)
        btn_operator.clicked.connect(self.show_message)

        btn_operator = QPushButton('clear', self)
        btn_operator.setGeometry(400, 350, 70, 30)
        btn_operator.clicked.connect(self.show_message)

        self.show()

    def show_message(self):

        next_input = self.sender().text()  # button value.
        current_result_text = self.text_shown.text()
        operators = ('+', '-', '*', '/', '=')
        operators1 = ('+', '-', '*', '/')
        operators2 = ('=')

        self.message_show.setText('')

        def show():
            self.text_shown.setText(current_result_text + str(next_input))
            self.status = 1
            self.currentInput = next_input

        def result_operation_show():
            print(str(self.result) + str(next_input))
            self.text_shown.setText(str(self.result) + str(next_input))
            self.status = 1
            self.currentInput = next_input

        def clear_show():
            self.text_shown.setText(str(next_input))
            self.status = 1
            self.currentInput = next_input

        def eval_show():
            result = ''
            try:
                result = eval(current_result_text)
            except SyntaxError:
                self.message_show.setText('Wrong input')
            except Exception as exception:
                print(exception)
                self.message_show.setText('Wrong input: ' + str(exception))
            self.result = result
            self.text_shown.setText(current_result_text + '=' + str(result))
            self.status = 2
            self.currentInput = '='

        def clear():
            self.text_shown.setText('0')
            self.status = 0
            self.currentInput = ''

        if next_input == 'clear':
            clear()
        else:
            if self.currentInput in operators:
                if self.currentInput in operators1:
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
