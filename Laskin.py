import PyQt5.QtWidgets as qtw

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Laskuri")
        # ↑ Valmistellaan ikkuna, peritään qwidgetin ominaisuudet
        # ↓ asetetaan layout sovellukselle
        self.setLayout(qtw.QVBoxLayout())
        self.keypad()
        self.temp_num = []
        self.fin_num = []

        # ↓ näyttää luokan
        self.show()


    def keypad(self):
        container = qtw.QWidget()
        container.setLayout(qtw.QGridLayout())
    
        # nappulat
        self.result_field = qtw.QLineEdit()
        btn_result = qtw.QPushButton('Enter', clicked = self.result)
        btn_clear = qtw.QPushButton('Clear', clicked = self.clear)
        btn_0 = qtw.QPushButton('0', clicked = lambda:self.num_press('0'))
        btn_1 = qtw.QPushButton('1', clicked = lambda:self.num_press('1'))
        btn_2 = qtw.QPushButton('2', clicked = lambda:self.num_press('2'))
        btn_3 = qtw.QPushButton('3', clicked = lambda:self.num_press('3'))
        btn_4 = qtw.QPushButton('4', clicked = lambda:self.num_press('4'))
        btn_5 = qtw.QPushButton('5', clicked = lambda:self.num_press('5'))
        btn_6 = qtw.QPushButton('6', clicked = lambda:self.num_press('6'))
        btn_7 = qtw.QPushButton('7', clicked = lambda:self.num_press('7'))
        btn_8 = qtw.QPushButton('8', clicked = lambda:self.num_press('8'))
        btn_9 = qtw.QPushButton('9', clicked = lambda:self.num_press('9'))
        btn_plus = qtw.QPushButton('+', clicked = lambda:self.func_press('+'))
        btn_minus = qtw.QPushButton('-', clicked = lambda:self.func_press('-'))
        btn_mult = qtw.QPushButton('*', clicked = lambda:self.func_press('*'))
        btn_div = qtw.QPushButton('÷', clicked = lambda:self.func_press('/'))

        # lisätään ↑ (lisättävä, rivi, sarake, korkeus, leveys)
        container.layout().addWidget(self.result_field, 0, 0, 1, 4)
        container.layout().addWidget(btn_9, 2, 2)
        container.layout().addWidget(btn_8, 2, 1)
        container.layout().addWidget(btn_7, 2, 0)
        container.layout().addWidget(btn_6, 3, 2)
        container.layout().addWidget(btn_5, 3, 1)
        container.layout().addWidget(btn_4, 3, 0)
        container.layout().addWidget(btn_3, 4, 2)
        container.layout().addWidget(btn_2, 4, 1)
        container.layout().addWidget(btn_1, 4, 0)
        container.layout().addWidget(btn_0, 5, 0, 1, 3)
        container.layout().addWidget(btn_clear, 1, 0, 1, 2)
        container.layout().addWidget(btn_result, 1, 2, 1, 2)
        container.layout().addWidget(btn_plus, 2, 3)
        container.layout().addWidget(btn_minus, 3, 3)
        container.layout().addWidget(btn_mult, 4, 3)
        container.layout().addWidget(btn_div, 5, 3)
        self.layout().addWidget(container)
        # tämä ↑ lisää napit lopulta layouttiin

    def num_press(self, num):
        self.temp_num.append(num)
        temp_string= "".join(self.temp_num)
        if self.fin_num:
            self.result_field.setText("".join(self.fin_num) + temp_string)
        else:
            self.result_field.setText("".join(temp_string))

    def func_press(self, func):
        temp_string = "".join(self.temp_num)
        self.fin_num.append(temp_string)
        self.fin_num.append(func)
        self.temp_num = []
        self.result_field.setText("".join(self.fin_num))

    def result(self):
        try:
            forbid = ['+', '-', '*', '/']
            for item in forbid:
                if self.fin_num[-1] == item and not self.temp_num:
                    return
            fin_string = "".join(self.fin_num) + "".join(self.temp_num)
            result_string = eval(fin_string)
            fin_string += '='
            fin_string += str(result_string)
            self.result_field.setText(fin_string)
            self.temp_num = []
            self.fin_num = []
        except ZeroDivisionError:
            self.temp_num = []
            return

    
    def clear(self):
        self.result_field.clear()
        self.temp_num = []
        self.fin_num = []

app = qtw.QApplication([])
mw = MainWindow()
app.setStyle(qtw.QStyleFactory.create('Fusion'))
app.exec_()