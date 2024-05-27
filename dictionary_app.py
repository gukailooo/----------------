'''
Используемые библиотеки
'''
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QSpinBox, QLabel, QMessageBox, QInputDialog
from decimal import Decimal, getcontext
from functools import reduce


'''
Функции
'''
def sqrt_with_precision(get_number, precision=64):
    # Устанавливаем уровень точности
    getcontext().prec = precision - 1  # Добавляем дополнительные цифры для точности в расчетах
    
    try:
        return str(Decimal(get_number).sqrt())
    except ValueError:
        return "Нельзя извлечь корень"
    
'''
Приложение
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
        layout.addWidget(self.generate_button_with_sqrt)
        layout.addWidget(self.generate_button_with_const)
        
        self.setLayout(layout)
        self.setWindowTitle('Генератор паролей')
        self.setGeometry(500, 500, 500, 500)


    def generate_passwords_with_square_sqrt(self):
        count = self.spin_box.value()
        if count >= 1:
            with open('passwords.txt', 'w') as file:
                for i in range(1, count+1):
                    result = sqrt_with_precision(i, 64)
                    if result!= "Нельзя извлечь корень":
                        file.write(f"{i}: {result}\n")
            QMessageBox.information(self, "Уведомление", "Пароли успешно записаны.")

    def generate_passwords_with_cubic_sqrt(self):
        count = self.spin_box.value()
        if count >= 1:
            with
        result = pow(9, 1/3)
        formatted_result = "{:.64f}".format(result)
        return formatted_result

    def generate_passwords_with_const(self):
        # Отношение длины окружности к ее диаметру
        value_pi = '3.14159265358979323846264338327950288419716939937510582097494459'
        # Отношение длины окружности к ее радиусу. Эквивалентно 2pi
        value_tau =  '6.28318530717958647692528676655900576839433879875021164194988918'


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())
