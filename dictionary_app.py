'''
Используемые библиотеки
'''
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QSpinBox, QLabel, QMessageBox, QInputDialog
from decimal import Decimal, getcontext
from functools import reduce
import math
from mpmath import *

    
'''
Программная реализация
'''

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        layout = QVBoxLayout()
        
        self.generate_button_with_square_sqrt = QPushButton("Сгенерировать пароли вычислением квадратного корня числа")
        self.generate_button_with_square_sqrt.clicked.connect(self.generate_passwords_with_square_sqrt)

        self.spin_box = QSpinBox(self)
        self.spin_box.setRange(1, 1000)  # Установка диапазона значений
        self.spin_box.setValue(1)  # Значение по умолчанию

        self.generate_button_with_cubic_sqrt = QPushButton("Сгенерировать пароли вычислением кубического корня числа")
        self.generate_button_with_cubic_sqrt.clicked.connect(self.generate_passwords_with_cubic_sqrt)


        self.generate_button_with_const = QPushButton("Сгенерировать пароли из известных констант")
        self.generate_button_with_const.clicked.connect(self.generate_passwords_with_const)

        label1 = QLabel("Введите количество паролей, которые необходимо сгенерировать:")
        layout.addWidget(label1)
        layout.addWidget(self.spin_box)
        label2 = QLabel("Выберите каким способом сгенерировать пароли:")
        layout.addWidget(label2)
        layout.addWidget(self.generate_button_with_square_sqrt)
        layout.addWidget(self.generate_button_with_cubic_sqrt)
        layout.addWidget(self.generate_button_with_const)
        
        self.setLayout(layout)
        self.setWindowTitle('Генератор паролей')
        self.setGeometry(500, 500, 500, 500)


    def generate_passwords_with_square_sqrt(self):
        count = self.spin_box.value()
        if count >= 1:
            with open('square_root_passwords.txt', 'w') as file:
                for i in range(1, count+1):
                    result = "{:.62f}".format(math.sqrt(i))
                    if result!= "Нельзя извлечь корень":
                        file.write(f"{i}: {result}\n")
            QMessageBox.information(self, "Уведомление", "Пароли успешно записаны.")


    def generate_passwords_with_cubic_sqrt(self):
        count = self.spin_box.value()
        if count >= 1:
            with open('cubic_root_passwords.txt', 'w') as file:
                for i in range(1, count+1):
                    # Вычисляем кубический корень числа i и форматируем результат до 64 знаков после запятой
                    result = "{:.62f}".format(pow(i, 1/3))
                    file.write(f"{i}: {result}\n")
            QMessageBox.information(self, "Уведомление", "Пароли успешно записаны.")


    def generate_passwords_with_const(self):
        count = self.spin_box.value()
        mp.dps = 63; mp.pretty = True

        value_pi = +pi # Отношение длины окружности к ее диаметру
        value_tau = 2*+pi # Отношение длины окружности к ее радиусу. Эквивалентно 2pi
        
        constants = [value_pi, value_tau]

        if count >= 1:
            with open('const_passwords.txt', 'w') as file:
                for i in range(1, count+1):
                    for j in constants:
                        file.write(f"{i}: {j}\n")
            QMessageBox.information(self, "Уведомление", "Пароли успешно записаны.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())
