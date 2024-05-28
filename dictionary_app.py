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
                    # result = "{:.62f}".format(math.sqrt(i))
                    result = math.sqrt(i)
                    if result!= "Нельзя извлечь корень":
                        file.write(f"Квадратный корень {i}: {result}\n")
            QMessageBox.information(self, "Уведомление", "Пароли успешно записаны.")


    def generate_passwords_with_cubic_sqrt(self):
        count = self.spin_box.value()
        if count >= 1:
            with open('cubic_root_passwords.txt', 'w') as file:
                for i in range(1, count+1):
                    # result = "{:.62f}".format(pow(i, 1/3))
                    result = pow(i, 1/3)
                    file.write(f"Кубический корень {i}: {result}\n")
            QMessageBox.information(self, "Уведомление", "Пароли успешно записаны.")


    def generate_passwords_with_const(self):
        count = self.spin_box.value()
        mp.dps = 63; mp.pretty = True

        value_pi = +pi # Отношение длины окружности к ее диаметру
        value_tau = 2*+pi # Отношение длины окружности к ее радиусу. Эквивалентно 2pi
        supergolden_ratio = (1 + pow((((29+3*math.sqrt(93)) / 2)), 1/3) + pow((((29-3*math.sqrt(93))/ 2)), 1/3)) / 3
        connective_constant_for_the_hexagonal_lattice = math.sqrt(2+math.sqrt(2))
        KeplerBouwkamp_constant = 0.11494204485329620070
        Wallis_constant = pow(((45-math.sqrt(1929)) / 18), 1/3) + pow(((45+math.sqrt(1929)) / 18), 1/3)
        the_number_e = math.e
        the_natural_logarithm_of_two = math.log(2)
        Lemniscate_constant = 2.62205755429211981046
        Eulers_constant = 0.57721566490153286060
        ErdosBorwein_constant = 1.60669515241529176378
        Omega_constant = 0.56714329040978387299
        Apéry's constant
        Laplace limit
        Soldner constant
        Gauss's constant
        Second Hermite constant
        Liouville's constant
        First continued fraction constant
        Ramanujan's constant

        mathematics_constants_dict = {'Значение pi': value_pi, 
                                'Значение tau(2pi)': value_tau, 
                                'Сверхзолотое сечение': supergolden_ratio,
                                'Соединительная константа для гексагональной решетки' : connective_constant_for_the_hexagonal_lattice,
                                'Постоянная Кеплера–Бувкампа' : KeplerBouwkamp_constant,
                                'Постоянная Уоллиса' : Wallis_constant,
                                'Число Эйлера' : the_number_e,
                                'Натуральный логарифм 2': the_natural_logarithm_of_two,
                                'Постоянная лемнискаты': Lemniscate_constant,
                                'Постоянная Эйлера': Eulers_constant,
                                'Постоянная Эрдеша–Борвейна': ErdosBorwein_constant,
                                'Постоянная Омега': Omega_constant,
                                'Константа Апери':
                                'Предел Лапласа'
                                'Константа Зельднера'
                                'Постоянная Гаусса'
                                'Вторая постоянная Эрмита'
                                'Постоянная Лиувилля'
                                'Первая непрерывная дробь константа'
                                'Постоянная Рамануджана'
                                'Постоянная Глейшера–Кинкелина'
                                'Константа Каталана'
                                'Число Дотти'
                                'Постоянная Мейсселя–Мертенса'
                                'Универсальная параболическая постоянная'
                                'Константа Каэна'
                                'Константа Гельфонда'
                                'Постоянная Гельфонда-Шнейдера'
                                'Вторая константа Фавара'
                                'Золотой угол'
                                'Константа Серпинского'
                                'Постоянная Ландау–Рамануджана'
                                'Первая постоянная Нильсена–Рамануджана'
                                'Константа Гизекинга'
                                'Постоянная Бернштейна'
                                'Константа Трибоначчи'
                                'Постоянная Бруна'
                                'Константа простых чисел - близнецов'
                                'Коэффициент пластичности'
                                'Постоянная Блоха'
                                'Z - балл для 97,5 процентиля'
                                'Постоянная Ландау'
                                'Третья постоянная Ландау'
                                'Постоянная Пруэ-Туэ–Морзе'
                                'Постоянная Голомба–Дикмана'
                                'Константа, связанная с асимптотическим поведением констант Лебега'
                                'Константа Феллера–Торнье'
                                'Константа Шамперноуна'
                                'Константа Салема'
                                'Константа Хинчина'
                                'Константа Леви (1)'
                                'Константа Леви (2)'
                                'Константа Коупленда–Эрдеша'
                                'Константа Миллса'
                                'Константа Гомперца'
                                'Постоянная де Брейна–Ньюмана'
                                'Постоянная Ван дер Пау'
                                'Магический угол'
                                'Постоянная Артина'
                                'Постоянная Портера'
                                'Постоянная Лох'
                                'Постоянная тессеракта Девиччи'
                                'Квадратная ледяная постоянная Либа'
                                'Постоянная Нивена'
                                'Константа Стивенса'
                                'Обычная последовательность сворачивания бумаги'
                                'Обратная постоянная Фибоначчи'
                                'Константа Хватала–Санкоффа для двоичного алфавита'
                                'Константа Фейгенбаума'
                                'Константы Чайтина'
                                'Константа Роббинса'
                                'Константа Вейерштрасса'
                                'Постоянная Франсена–Робинсона'
                                'Feigenbaum constant α'
                                'Вторая константа Дюбуа-Реймона'
                                'Постоянная Эрдеша–Тененбаума–Форда'
                                'Константа Конвея'
                                'Постоянная Хафнера–Сарнака-Маккерли'
                                'Константа Бэкхауса'
                                'Константа Вишваната'
                                'Постоянная Коморника–Лорети'
                                'Константа Эмбре–Трефетена'
                                'Постоянная Хита–Брауна-Мороза'
                                'Константа MRB'
                                'Простая константа'
                                'Квадратичная рекуррентная константа Сомоса'
                                'Постоянная Фояса'
                                'Логарифмическая емкость единичного диска'
                                'Константа Танигути'

                          }

        if count >= 1:
            with open('const_passwords.txt', 'w') as file:
                for name, value in constants_dict.items():
                    file.write(f"{name} : {value}\n")
            QMessageBox.information(self, "Уведомление", "Пароли успешно записаны.")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())
