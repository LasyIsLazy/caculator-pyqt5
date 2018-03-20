# coding = utf-8

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QHBoxLayout, QVBoxLayout, QGridLayout


class Calculator(QWidget):

    def __init__(self):
        self.status = 0  # 0: cleared; 1: calculating; 2: calculated.
        self.currentInput = ''
        self.result = 0
        self.text_shown = None
        self.message_show = None
        self.next_input = ''
        self.current_result_text = ''
        self.operators = ['+', '-', '*', '/', '=']
        self.operators1 = ['+', '-', '*', '/']
        self.operators2 = ['=']
        super().__init__()
        self.initUI()

    def initUI(self):
        width = 500
        height = 400
        self.setGeometry(300, 300, width, height)
        self.setWindowTitle('Calculator')
        # self.setWindowIcon(QIcon('xdbcb8.ico'))

        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        self.text_shown = QLineEdit('0', self)
        self.text_shown.setEnabled(False)
        self.text_shown.setMinimumHeight(60)
        main_layout.addWidget(self.text_shown)  # show expression and result.

        # buttons.
        btns_layout = QGridLayout()
        main_layout.addLayout(btns_layout)
        btns1 = ['clear', 'M', 'te', '+',
                 '1', '2', '3', '-',
                 '4', '5', '6', '*',
                 '7', '8', '9', '/',
                 '.', '0', '=']
        positions = ((i, j) for i in range(5) for j in range(4))
        for btn_name, position in zip(btns1, positions):
            btn = QPushButton(str(btn_name))
            btn.setMinimumHeight(50)
            btn.clicked.connect(self.show_message_judge)
            btns_layout.addWidget(btn, *position)

        # message output.
        self.message_show = QLineEdit('', self)  # show message when input is wrong.
        self.message_show.setEnabled(False)
        main_layout.addWidget(self.message_show)

        self.show()

    def show_message_judge(self):
        self.message_show.setText('Inputting...')
        self.next_input = self.sender().text()  # button value.
        self.current_result_text = self.text_shown.text()

        if self.next_input == 'clear':
            self.clear()
            self.message_show.setText('Cleared.')
        else:
            if self.currentInput in self.operators:
                if self.currentInput in self.operators1:
                    if self.next_input in self.operators:
                        return
                    else:
                        self.show_input()
                else:  # self.currentOperator in operators2
                    if self.next_input in self.operators:
                        if self.next_input in self.operators2:
                            return
                        else:  # next_input in operators1
                            self.result_operation_show()
                    else:
                        self.clear_show()
            else:
                if self.next_input in self.operators:
                    if self.next_input in self.operators1:
                        self.show_input()
                    else:  # next_input in operators2
                        self.eval_show()
                else:
                    if self.status == 0:
                        self.clear_show()
                    else:
                        self.show_input()

    def show_input(self):
        self.text_shown.setText(self.current_result_text + str(self.next_input))
        self.status = 1
        self.currentInput = self.next_input

    def result_operation_show(self):
        print(str(self.result) + str(self.next_input))
        self.text_shown.setText(str(self.result) + str(self.next_input))
        self.status = 1
        self.currentInput = self.next_input

    def clear_show(self):
        self.text_shown.setText(str(self.next_input))
        self.status = 1
        self.currentInput = self.next_input

    def eval_show(self):
        result = ''
        try:
            result = eval(self.current_result_text)
        except SyntaxError:
            self.message_show.setText('Wrong input')
        except Exception as exception:
            print(exception)
            self.message_show.setText('Wrong input: ' + str(exception))
        self.result = result
        self.text_shown.setText(self.current_result_text + '=' + str(result))
        self.status = 2
        self.currentInput = '='

    def clear(self):
        self.text_shown.setText('0')
        self.status = 0
        self.currentInput = ''


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Calculator()
    sys.exit(app.exec_())
