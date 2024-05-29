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


        self.generate_button_with_math_const = QPushButton("Сгенерировать пароли из известных математических констант")
        self.generate_button_with_math_const.clicked.connect(self.generate_passwords_with_math_const)

        self.generate_button_with_phys_const = QPushButton("Сгенерировать пароли из известных математических констант")
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


    def generate_passwords_with_math_const(self):
        count = self.spin_box.value()
        mp.dps = 63; mp.pretty = True

        value_pi = +pi # Отношение длины окружности к ее диаметру
        value_tau = 2*+pi # Отношение длины окружности к ее радиусу. Эквивалентно 2pi
        Supergolden_ratio = (1 + pow((((29+3*math.sqrt(93)) / 2)), 1/3) + pow((((29-3*math.sqrt(93))/ 2)), 1/3)) / 3
        Connective_constant_for_the_hexagonal_lattice = math.sqrt(2+math.sqrt(2))
        KeplerBouwkamp_constant = 0.11494204485329620070
        Wallis_constant = pow(((45-math.sqrt(1929)) / 18), 1/3) + pow(((45+math.sqrt(1929)) / 18), 1/3)
        the_number_e = math.e
        the_natural_logarithm_of_two = math.log(2)
        Lemniscate_constant = 2.62205755429211981046
        Eulers_constant = 0.57721566490153286060
        ErdosBorwein_constant = 1.60669515241529176378
        Omega_constant = 0.56714329040978387299
        Apery_constant = 1.20205690315959428539
        Laplace_limit = 0.66274341934918158097
        Soldner_constant = 1.45136923488338105028
        Gauss_constant = 0.83462684167407318628
        Second_Hermite_constant = 1.15470053837925152901
        Liouville_constant = 0.110001000000000000000001
        First_continued_fraction_constant = 0.69777465796400798201
        Ramanujan_constant = 262537412640768743.999999999999250073
        Glaisher_Kinkelin_constant = 1.28242712910062263687
        Catalan_constant = 0.91596559417721901505
        Dottie_number = 0.73908513321516064165
        Meissel_Mertens_constant = 0.26149721284764278375
        Universal_parabolic_constant = 2.29558714939263807403
        Cahen_constant = 0.64341054628833802618
        Gelfond_constant = 23.1406926327792690057
        Gelfond_Schneider_constant = 2.66514414269022518865
        Second_Favard_constant = 1.23370055013616982735
        Golden_angle = 2.39996322972865332223
        Sierpinski_constant = 2.58498175957925321706
        Landau_Ramanujan_constant = 0.76422365358922066299
        First_Nielsen_Ramanujan_constant = 0.82246703342411321823
        Gieseking_constant = 1.01494160640965362502
        Bernstein_constant = 0.28016949902386913303
        Tribonacci_constant = 1.83928675521416113255
        Brun_constant = 1.902160583104
        Twin_primes_constant = 0.66016181584686957392
        Plastic_ratio = 1.32471795724474602596
        Z_score_for_the_97_5_percentile_point = 1.95996398454005423552
        Prouhet_Thue_Morse_constant = 0.41245403364010759778
        Golomb_Dickman_constant = 0.62432998854355087099
        Constant_related_to_the_asymptotic_behavior_of_Lebesgue_constants = 0.98943127383114695174
        Feller_Tornier_constant = 0.66131704946962233528
        Champernowne_constant = 0.12345678910111213141
        Salem_constant = 1.17628081825991750654
        Khinchin_constant = 2.68545200106530644530
        Levy_constant_1 = 1.18656911041562545282
        Levy_constant_2 = 3.27582291872181115978
        Copeland_Erdos_constant = 0.23571113171923293137
        Mills_constant = 1.30637788386308069046
        Gompertz_constant = 0.59634736232319407434
        Van_der_Pauw_constant = 4.53236014182719380962
        Magic_angle = 0.955316618124509278163
        Artin_constant = 0.37395581361920228805
        Porter_constant = 1.46707807943397547289
        Lochs_constant = 0.97027011439203392574
        DeVicci_tesseract_constant = 1.00743475688427937609
        Lieb_square_ice_constant = 1.53960071783900203869
        Niven_constant = 1.70521114010536776428
        Stephens_constant = 0.57595996889294543964
        Regular_paperfolding_sequence = 0.85073618820186726036
        Reciprocal_Fibonacci_constant = 3.35988566624317755317
        Feigenbaum_constant = 4.66920160910299067185
        Chaitin_constants = 0.0078749969978123844
        Robbins_constant = 0.66170718226717623515
        Weierstrass_constant = 0.47494937998792065033
        Fransen_Robinson_constant = 2.80777024202851936522
        Feigenbaum_constant_a = 2.50290787509589282228
        Second_du_Bois_Reymond_constant = 0.19452804946532511361
        Erdos_Tenenbaum_Ford_constant = 0.08607133205593420688
        Conway_constant = 1.30357726903429639125
        Hafner_Sarnak_McCurley_constant = 0.35323637185499598454
        Backhouse_constant = 1.45607494858268967139
        Viswanath_constant = 1.1319882487943
        Komornik_Loreti_constant = 1.78723165018296593301
        Embree_Trefethen_constant = 0.70258
        Heath_Brown_Moroz_constant = 0.00131764115485317810
        MRB_constant = 0.18785964246206712024
        Prime_constant = 0.41468250985111166024
        Somos_quadratic_recurrence_constant = 1.66168794963359412129
        Foias_constant = 1.18745235112650105459
        Logarithmic_capacityo_the_unit_disk = 0.59017029950804811302
        Taniguchi_constant = 0.67823449191739197803



        mathematics_constants_dict = {'Значение pi': value_pi, 
                                'Значение tau(2pi)': value_tau, 
                                'Сверхзолотое сечение': Supergolden_ratio,
                                'Соединительная константа для гексагональной решетки' : Connective_constant_for_the_hexagonal_lattice,
                                'Постоянная Кеплера–Бувкампа' : KeplerBouwkamp_constant,
                                'Постоянная Уоллиса' : Wallis_constant,
                                'Число Эйлера' : the_number_e,
                                'Натуральный логарифм 2': the_natural_logarithm_of_two,
                                'Постоянная лемнискаты': Lemniscate_constant,
                                'Постоянная Эйлера': Eulers_constant,
                                'Постоянная Эрдеша–Борвейна': ErdosBorwein_constant,
                                'Постоянная Омега': Omega_constant,
                                'Константа Апери': Apery_constant,
                                'Предел Лапласа' : Laplace_limit,
                                'Константа Зельднера' : Soldner_constant,
                                'Постоянная Гаусса' : Gauss_constant,
                                'Вторая постоянная Эрмита' : Second_Hermite_constant,
                                'Постоянная Лиувилля' : Liouville_constant,
                                'Первая непрерывная дробь константа' : First_continued_fraction_constant,
                                'Постоянная Рамануджана' : Ramanujan_constant,
                                'Постоянная Глейшера–Кинкелина' : Glaisher_Kinkelin_constant,
                                'Константа Каталана' : Catalan_constant,
                                'Число Дотти' : Dottie_number,
                                'Постоянная Мейсселя–Мертенса' : Meissel_Mertens_constant,
                                'Универсальная параболическая постоянная' : Universal_parabolic_constant,
                                'Константа Каэна' : Cahen_constant,
                                'Константа Гельфонда' : Gelfond_constant,
                                'Постоянная Гельфонда-Шнейдера' : Gelfond_Schneider_constant,
                                'Вторая константа Фавара' : Second_Favard_constant,
                                'Золотой угол' : Golden_angle,
                                'Константа Серпинского' : Sierpinski_constant,
                                'Постоянная Ландау–Рамануджана' : Landau_Ramanujan_constant,
                                'Первая постоянная Нильсена–Рамануджана' : First_Nielsen_Ramanujan_constant,
                                'Константа Гизекинга' : Gieseking_constant,
                                'Постоянная Бернштейна' : Bernstein_constant,
                                'Константа Трибоначчи' : Tribonacci_constant,
                                'Постоянная Бруна' : Brun_constant,
                                'Константа простых чисел - близнецов' : Twin_primes_constant,
                                'Коэффициент пластичности' : Plastic_ratio,
                                'Z - балл для 97,5 процентиля' : Z_score_for_the_97_5_percentile_point,
                                'Постоянная Пруэ-Туэ–Морзе' : Prouhet_Thue_Morse_constant,
                                'Постоянная Голомба–Дикмана' : Golomb_Dickman_constant,
                                'Константа, связанная с асимптотическим поведением констант Лебега' : Constant_related_to_the_asymptotic_behavior_of_Lebesgue_constants,
                                'Константа Феллера–Торнье' : Feller_Tornier_constant,
                                'Константа Шамперноуна' : Champernowne_constant,
                                'Константа Салема' : Salem_constant, 
                                'Константа Хинчина' : Khinchin_constant,
                                'Константа Леви (1)' : Levy_constant_1,
                                'Константа Леви (2)' : Levy_constant_2,
                                'Константа Коупленда–Эрдеша' : Copeland_Erdos_constant,
                                'Константа Миллса' : Mills_constant,
                                'Константа Гомперца' : Gompertz_constant,
                                'Постоянная Ван дер Пау' : Van_der_Pauw_constant,
                                'Магический угол' : Magic_angle,
                                'Постоянная Артина' : Artin_constant,
                                'Постоянная Портера' : Porter_constant,
                                'Постоянная Лох' : Lochs_constant,
                                'Постоянная тессеракта Девиччи' : DeVicci_tesseract_constant,
                                'Квадратная ледяная постоянная Либа' : Lieb_square_ice_constant,
                                'Постоянная Нивена' : Niven_constant,
                                'Константа Стивенса' : Stephens_constant,
                                'Обычная последовательность сворачивания бумаги' : Regular_paperfolding_sequence,
                                'Обратная постоянная Фибоначчи' : Reciprocal_Fibonacci_constant,
                                'Константа Фейгенбаума' : Feigenbaum_constant,
                                'Константы Чайтина' : Chaitin_constants,
                                'Константа Роббинса' : Robbins_constant,
                                'Константа Вейерштрасса' : Weierstrass_constant,
                                'Постоянная Франсена–Робинсона' : Fransen_Robinson_constant,
                                'Feigenbaum constant α' : Feigenbaum_constant_a,
                                'Вторая константа Дюбуа-Реймона' : Second_du_Bois_Reymond_constant,
                                'Постоянная Эрдеша–Тененбаума–Форда' : Erdos_Tenenbaum_Ford_constant,
                                'Константа Конвея' : Conway_constant,
                                'Постоянная Хафнера–Сарнака-Маккерли' : Hafner_Sarnak_McCurley_constant,
                                'Константа Бэкхауса' : Backhouse_constant,
                                'Константа Вишваната' : Viswanath_constant,
                                'Постоянная Коморника–Лорети' : Komornik_Loreti_constant,
                                'Константа Эмбре–Трефетена' : Embree_Trefethen_constant,
                                'Постоянная Хита–Брауна-Мороза' : Heath_Brown_Moroz_constant,
                                'Константа MRB' : MRB_constant,
                                'Простая константа' : Prime_constant,
                                'Квадратичная рекуррентная константа Сомоса' : Somos_quadratic_recurrence_constant,
                                'Постоянная Фояса' : Foias_constant,
                                'Логарифмическая емкость единичного диска' : Logarithmic_capacityo_the_unit_disk,
                                'Константа Танигути' : Taniguchi_constant,

                          }

        if count >= 1:
            with open('const_passwords.txt', 'w') as file:
                for name, value in mathematics_constants_dict.items():
                    file.write(f"{name} : {value}\n")
            QMessageBox.information(self, "Уведомление", "Пароли успешно записаны.")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())
