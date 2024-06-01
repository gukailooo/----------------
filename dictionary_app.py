'''
Используемые библиотеки
'''
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QPushButton, QSpinBox, QLabel, 
                             QMessageBox, QMainWindow, QComboBox, QDialog, QLineEdit, QHBoxLayout)
from PyQt5.QtGui import QDoubleValidator, QPixmap, QIcon
from PyQt5.QtCore import Qt
import math
from mpmath import *
import pandas as pd
import openpyxl
    
'''
Программная реализация
'''

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

        
    def initUI(self):
        layout = QVBoxLayout()
        
        self.setLayout(layout)
        self.setWindowTitle('Генератор паролей')
        self.setGeometry(100, 100, 700, 700)

        self.setWindowIcon(QIcon(r"password.png")) 

        self.generate_button_with_square_sqrt = QPushButton('Сгенерировать пароли вычислением квадратного корня числа')
        self.generate_button_with_square_sqrt.clicked.connect(self.generate_passwords_with_square_sqrt)

        self.spin_box = QSpinBox(self)
        self.spin_box.setRange(1, 999999)  # Установка диапазона значений
        self.spin_box.setValue(1)  # Значение по умолчанию

        self.generate_button_with_cubic_sqrt = QPushButton('Сгенерировать пароли вычислением кубического корня числа')
        self.generate_button_with_cubic_sqrt.clicked.connect(self.generate_passwords_with_cubic_sqrt)

        self.generate_button_with_math_const = QPushButton('Сгенерировать пароли из известных математических констант')
        self.generate_button_with_math_const.clicked.connect(self.generate_passwords_with_math_const)

        self.generate_button_with_physical_const = QPushButton('Сгенерировать пароли из известных физических констант')
        self.generate_button_with_physical_const.clicked.connect(self.generate_passwords_with_physical_const)

        self.generate_button_with_table_bradis = QPushButton('Сгенерировать пароли из таблицы Брадиса')
        self.generate_button_with_table_bradis.clicked.connect(self.generate_passwords_with_table_bradis)

        self.generate_button_with_rec_relations = QPushButton('Сгенерировать пароли из рекуррентных соотношений')
        self.generate_button_with_rec_relations.clicked.connect(self.select_recurrent_relation)

        label1 = QLabel('Введите количество паролей, которые необходимо сгенерировать:')
        layout.addWidget(label1)
        layout.addWidget(self.spin_box)
        label2 = QLabel('Выберите каким способом сгенерировать пароли:')
        layout.addWidget(label2)
        layout.addWidget(self.generate_button_with_square_sqrt)
        layout.addWidget(self.generate_button_with_cubic_sqrt)
        layout.addWidget(self.generate_button_with_math_const)
        layout.addWidget(self.generate_button_with_physical_const)
        layout.addWidget(self.generate_button_with_table_bradis)
        layout.addWidget(self.generate_button_with_rec_relations)

    # Генерация паролей на основе вычисления квадратного корня
    def generate_passwords_with_square_sqrt(self):
        count = self.spin_box.value()
        if count >= 1:
            with open('square_root_passwords.txt', 'w') as file:
                file.write(f'Вычисление квадратного корня от номера пароля.')
                for i in range(1, count+1):
                    # result = "{:.62f}".format(math.sqrt(i))
                    result = math.sqrt(i)
                    if result!= 'Нельзя извлечь корень':
                        file.write(f'Квадратный корень {i}: {result}\n')
            QMessageBox.information(self, 'Уведомление', 'Пароли успешно записаны.')



    # Генерация паролей на основе вычисления кубического корня
    def generate_passwords_with_cubic_sqrt(self):
        count = self.spin_box.value()
        if count >= 1:
            with open('cubic_root_passwords.txt', 'w') as file:
                file.write(f'Вычисление кубического корня от номера пароля.')
                for i in range(1, count+1):
                    # result = "{:.62f}".format(pow(i, 1/3))
                    result = pow(i, 1/3)
                    file.write(f'Кубический корень {i}: {result}\n')
            QMessageBox.information(self, 'Уведомление', 'Пароли успешно записаны.')




    # Генерация паролей на основе математических констант
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
        Bazilio_constant = 1.504
        Dirichlet_constant = 1.2824
        constant_Turing = 0.353236371854995
        Lindelof_constant = 0.5
        Sylvestr_constant = 2.337
        Legendre_constant = 1.13198824
        Rappaport_constant = 0.888899
        The_Turing_Mainzel_constant = 0.574713
        Dudik_constant = 0.876627
        Bauer_constant = 1.543377
        Golombo_constant = 0.62432998854355
        Plat_constant = 0.927054
        Neper_constant = 1.915319464183
        Caprekar_constant = 6174
        Pierce_constant = 1.291285997062663
        Lambert_constant = 0.567143290409784
        Euler_Brunowy_constant = 1.606695152415291
        Homer_constant = 0.824
        Fejer_constant = 1.202056903159594
        constant_pi_2 = math.pi / 2
        constant_pi_3 = math.pi / 3
        constant_pi_4 = math.pi / 4
        


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
                                'Константа Базилио' : Bazilio_constant,
                                'Константа Дирихле' : Dirichlet_constant,
                                'Константа Тюринга' : constant_Turing,
                                'Константа Линделофа' : Lindelof_constant,
                                'Константа Сильвестра' : Sylvestr_constant,
                                'Константа Лежандра' : Legendre_constant,
                                'Константа Раппопорта' : Rappaport_constant,
                                'Константа Тьюринга-Майнцела' : The_Turing_Mainzel_constant,
                                'Константа Дюдика' : Dudik_constant,
                                'Константа Бауэра' : Bauer_constant,
                                'Константа Голомбо' : Golombo_constant,
                                'Константа Плата' : Plat_constant,
                                'Константа Непера' : Neper_constant,
                                'Константа Капрекара' : Caprekar_constant,
                                'Константа Пирса' : Pierce_constant,
                                'Константа Ламберта' : Lambert_constant,
                                'Константа Эйлера-Бруноуи' : Euler_Brunowy_constant,
                                'Константа Гомера' : Homer_constant,
                                'Константа Фейера' : Fejer_constant,
                                'Постоянная Пи-два' : constant_pi_2,
                                'Постоянная Пи-три' : constant_pi_3,
                                'Постоянная Пи-четыре' : constant_pi_4,

                          }

        # if count >= 1:
        #     with open('mathematics_const_passwords.txt', 'w') as file:
        #         file.write('Известные математические константы(до 64 знаков):')
        #         for name, value in mathematics_constants_dict.items():
        #             file.write(f"{name} : {value}\n")
        #     QMessageBox.information(self, 'Уведомление', 'Пароли успешно записаны.')
        if count >= 1:
            df = pd.DataFrame(list(mathematics_constants_dict.items()), columns=['Название константы', 'Значение'])
            df.to_excel('mathematics_const_passwords.xlsx', index=False)

            QMessageBox.information(self, 'Уведомление', 'Пароли успешно записаны в Excel файл.')
    


    # Генерация паролей на основе физических констант
    def generate_passwords_with_physical_const(self):
        count = self.spin_box.value()

        speed_of_light_in_vacuum = 299792458
        Planck_constant = 6.62607015e-34
        reduced_Planck_constant = 1.054571817e-34
        vacuum_magnetic_permeability = 1.25663706127e-06
        characteristic_impedance_of_vacuum = 376.730313412
        vacuum_electric_permittivity = 8.8541878188e-12
        Boltzmann_constant = 1.380649e-23
        Newtonian_constant_of_gravitation = 6.6743e-11
        Coulomb_constant = 8.9875517923e+09
        cosmological_constant = 1.089e-52
        Stefan_Boltzmann_constant = 5.670374419e-08
        first_radiation_constant = 3.741771852e-16
        first_radiation_constant_for_spectral_radiance = 1.191042972e-16
        second_radiation_constant = 1.438776877e-02
        Wien_wavelength_displacement_law_constant =2.897771955e-03
        Wien_frequency_displacement_law_constant = 5.878925757e+10
        Wien_entropy_displacement_law_constant = 3.002916077e-03
        elementary_charge = 1.602176634e-19
        conductance_quantum = 7.748091729e-05
        inverse_conductance_quantum = 12906.40372
        von_Klitzing_constant = 25812.80745
        Josephson_constant = 4.835978484e+14
        magnetic_flux_quantum = 2.067833848e-15
        fine_structure_constant = 0.0072973525643
        inverse_fine_structure_constant = 137.035999177
        electron_mass = 9.1093837139e-31
        muon_mass = 1.883531627e-28
        tau_mass = 3.16754e-27
        proton_mass = 1.67262192595e-27
        neutron_mass = 1.67492750056e-27
        top_quark_mass = 3.0784e-25
        proton_to_electron_mass_ratio = 1836.152673426
        W_to_Z_mass_ratio = 0.88145
        weak_mixing_angle = 0.2229
        electron_g_factor = -2.00231930436092
        muon_g_factor = -2.00233184123
        proton_g_factor = 5.5856946893
        quantum_of_circulation = 3.6369475467e-04
        Bohr_magneton = 9.2740100657e-24
        nuclear_magneton = 5.0507837393e-27
        classical_electron_radius = 2.8179403205e-15
        Thomson_cross_section = 6.6524587051e-29
        Bohr_radius = 5.29177210544e-11
        Hartree_energy = 4.359744722206e-18
        Rydberg_unit_of_energy = 2.179872361103e-18
        Rydberg_constant = 10973731.568157
        Fermi_coupling_constant = 1.1663787e-05
        Avogadro_constant = 6.02214076e+23
        molar_gas_constant = 8.31446261815324
        Faraday_constant = 96485.33212331002
        molar_Planck_constant = 3.9903127128934314e-10
        atomic_mass_of_carbon_12 = 1.99264687992e-26
        molar_mass_of_carbon_12 = 0.012
        atomic_mass_constant = 1.66053906892e-27
        molar_mass_constant = 0.001
        molar_volume_of_silicon = 1.205883199e-05
        hyperfine_transition_frequency_of_133Cs = 9192631770
        the_fine_structure_constant = 7.2973525643e-3
        Planck_mass = 2.176434e-8
        Planck_length = 1.616255e-35
        Planck_time = 5.391247e-44
        Planck_temperature = 1.416784
        The_temperature_of_the_triple_point_of_water = 273,16

        physical_constants_dict = {'Скорость света в вакууме' : speed_of_light_in_vacuum,
                                   'Постоянная Планка' : Planck_constant,
                                   'Уменьшенная постоянная Планка' : reduced_Planck_constant,
                                   'Магнитная проницаемость вакуума' : vacuum_magnetic_permeability,
                                   'Характеристическое сопротивление вакуума' : characteristic_impedance_of_vacuum,
                                   'Электрическая диэлектрическая проницаемость вакуума' : vacuum_electric_permittivity,
                                   'Постоянная Больцмана' : Boltzmann_constant,
                                   'Ньютоновская постоянная тяготения(гравитационная постоянная)' : Newtonian_constant_of_gravitation,
                                   'Кулоновская постоянная' : Coulomb_constant,
                                   'Космологическая постоянная' : cosmological_constant,
                                   'Постоянная Стефана–Больцмана' : Stefan_Boltzmann_constant,
                                   'Первая постоянная излучения' : first_radiation_constant,
                                   'Первая постоянная излучения для спектрального сияния' : first_radiation_constant_for_spectral_radiance,
                                   'Вторая постоянная излучения' : second_radiation_constant,
                                   'Постоянная закона смещения длины волны Вина' : Wien_wavelength_displacement_law_constant,
                                   'Постоянная закона частотного смещения Вина' : Wien_frequency_displacement_law_constant,
                                   'Постоянная закона смещения энтропии Вина' : Wien_entropy_displacement_law_constant,
                                   'Элементарный заряд' : elementary_charge,
                                   'Квант проводимости' : conductance_quantum,
                                   'Квант обратной проводимости' : inverse_conductance_quantum,
                                   'Постоянная вон Клицинга' : von_Klitzing_constant,
                                   'Константа Джозефсона' : Josephson_constant,
                                   'Квант магнитного потока' : magnetic_flux_quantum,
                                   'Константа тонкой структуры' : fine_structure_constant,
                                   'Обратная константа тонкой структуры' : inverse_fine_structure_constant,
                                   'Масса электрона' : electron_mass,
                                   'Масса мюона' : muon_mass,
                                   'Масса тау' : tau_mass,
                                   'Масса протона' : proton_mass,
                                   'Масса нейтрона' : neutron_mass,
                                   'Масса верхнего кварка' : top_quark_mass,
                                   'Отношение массы протона к массе электрона' : proton_to_electron_mass_ratio,
                                   'Отношение массы W к Z' : W_to_Z_mass_ratio,
                                   'Слабый угол смешивания' : weak_mixing_angle,
                                   'g-фактор электрона' : electron_g_factor,
                                   'g мюонный фактор' : muon_g_factor,
                                   'Протонный g-фактор' : proton_g_factor,
                                   'Квант циркуляции' : quantum_of_circulation,
                                   'Магнетон Бора' : Bohr_magneton,
                                   'Ядерный магнетон' : nuclear_magneton,
                                   'Классический радиус электрона' : classical_electron_radius,
                                   'Томсон сечение' : Thomson_cross_section, 
                                   'Радиус Бора' : Bohr_radius,
                                   'Энергия Хартри' : Hartree_energy,
                                   'Ридберговская единица энергии' : Rydberg_unit_of_energy,
                                   'Постоянная Ридберга' : Rydberg_constant,
                                   'Константа связи Ферми' : Fermi_coupling_constant,
                                   'Константа Авогадро' : Avogadro_constant,
                                   'Молярная газовая постоянная' : molar_gas_constant,
                                   'Постоянная Фарадея' : Faraday_constant,
                                   'Молярная постоянная Планка' : molar_Planck_constant,
                                   'Атомная масса из углерод-12' : atomic_mass_of_carbon_12,
                                   'Молярная масса из углерод-12' : molar_mass_of_carbon_12,
                                   'Постоянная атомной массы' : atomic_mass_constant,
                                   'Постоянная молярной массы' : molar_mass_constant,
                                   'Молярный объем кремния' : molar_volume_of_silicon,
                                   'Частота сверхтонких переходов 133Cs' : hyperfine_transition_frequency_of_133Cs,
                                   'Постоянная тонкой структуры' : the_fine_structure_constant,
                                   'Планковская масса' : Planck_mass,
                                   'Планковская длина' : Planck_length,
                                   'Планковское время' : Planck_time,
                                   'Планковская температура' : Planck_temperature,
                                   'Температура тройной точки воды' : The_temperature_of_the_triple_point_of_water,
 
        }

        # if count >= 1:
        #     with open('physical_const_passwords.txt', 'w') as file:
        #         file.write('Физические константы(до 64 знаков):')
        #         for name, value in physical_constants_dict.items():
        #             file.write(f"{name} : {value}\n")
        #     QMessageBox.information(self, 'Уведомление', 'Пароли успешно записаны.')
        
        if count >= 1:
            df = pd.DataFrame(list(physical_constants_dict.items()), columns=['Название константы', 'Значение'])
            df.to_excel('physical_const_passwords.xlsx', index=False)

            QMessageBox.information(self, 'Уведомление', 'Пароли успешно записаны в Excel файл.')


    # Таблица Брадиса
    def generate_passwords_with_table_bradis(self):
        bradis_table = {}
        for angle in range(0, 91):  # Углы от 0 до 90 градусов
            rad = math.radians(angle)
            bradis_table[angle] = {
        'sin': round(math.sin(rad), 8),
        'cos': round(math.cos(rad), 8),
        'tan': round(math.tan(rad), 8) if angle != 90 else 'inf',  # tan 90° -> бесконечность
        'cot': round(1 / math.tan(rad), 8) if angle != 0 else 'inf'  # cot 0° -> бесконечность
    }

        wb = openpyxl.Workbook()
        ws = wb.active
        ws.append(['Угол (градусы)', 'sin', 'cos', 'tan', 'cot'])

        for angle, values in bradis_table.items():
            ws.append([angle, values['sin'], values['cos'], values['tan'], values['cot']])


        file_path = 'bradis_table_passwords.xlsx'
        wb.save(file_path)

        QMessageBox.information(self, 'Уведомление', 'Пароли успешно записаны в Excel файл.')

    


    # Генерация паролей на основе рекуррентных соотношений
    def generate_passwords_with_recurrent_relation(self, relation, dialog):
        dialog.accept()
        if relation == 'Последовательность Фибоначчи':
            self.generate_passwords_with_fibonacci()    
        elif relation == 'Арифметическая прогрессия':
            self.generate_passwords_with_arithmetic_progression()
        elif relation == 'Геометрическая последовательность':
            self.generate_passwords_with_geometric_progression()
        elif relation == 'Последовательность с добавлением константы':
            self.prompt_for_constant()
        elif relation == 'Числа Каталана':
            self.generate_passwords_with_catalan_numbers()

    def select_recurrent_relation(self):
        dialog = QDialog(self)
        dialog.setWindowTitle('Выбор рекуррентного соотношения')
        layout = QVBoxLayout()

        combo_box = QComboBox(dialog)
        combo_box.addItem('Последовательность Фибоначчи')
        combo_box.addItem('Арифметическая прогрессия')
        combo_box.addItem('Геометрическая прогрессия')
        combo_box.addItem('Последовательность с добавлением константы')
        combo_box.addItem('Числа Каталана')

        select_button = QPushButton("Выбрать", dialog)
        select_button.clicked.connect(lambda: self.generate_passwords_with_recurrent_relation(combo_box.currentText(), dialog))

        layout.addWidget(QLabel('Выберите рекуррентное соотношение:'))
        layout.addWidget(combo_box)
        layout.addWidget(select_button)

        dialog.setLayout(layout)
        dialog.exec_()



    # последовательность Фибоначчи
    def fibonacci_iterative(self, n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        fib_sequence = [0, 1]
        for i in range(2, n + 1):
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence

    def generate_passwords_with_fibonacci(self, max_length=64):
        count = self.spin_box.value()
        if count < 1:
            QMessageBox.information(self, 'Уведомление', 'Количество паролей должно быть не менее 1.')
            return
        
        fibonacci_sequence = self.fibonacci_iterative(count)
        fib_string = ''.join(str(num) for num in fibonacci_sequence).replace('.', '')     
        passwords = [fib_string[i:i + max_length] for i in range(0, len(fib_string), max_length)]  
        passwords = passwords[:count]
        
        with open('fibonacci_sequences_passwords.txt', 'w') as file:
            file.write('Числа Фибоначчи - последовательность чисел, где каждое последующее число является суммой двух предшествующих.'
                       'Каждый новый пароль - это 64 символа от последовательности Фибоначчи:\n')
            for idx, password in enumerate(passwords, start=1):
                file.write(f"Password with fibonacci sequences {idx}: {password}\n")
        
        QMessageBox.information(self, 'Уведомление', 'Пароли успешно записаны.')

    

    # арифметическая прогрессия
    def arithmetic_progression(self, a1, d, n):
        return [a1 + i * d for i in range(n)]

    def generate_passwords_with_arithmetic_progression(self, max_length=64):
        count = self.spin_box.value()

        if count < 1:
            QMessageBox.information(self, "Уведомление", "Количество паролей должно быть не менее 1.")
            return
        
        a1 = 1  # Первый член
        d = 5   # Разность прогрессии

        arithmetic_sequence = self.arithmetic_progression(a1, d, 100000)
        arith_string = ''.join(str(num) for num in arithmetic_sequence)
        passwords = [arith_string[i:i + max_length] for i in range(0, len(arith_string), max_length)]
        passwords = passwords[:count]
        
        with open('arithmetic_progression_passwords.txt', 'w') as file:
            file.write('Каждый новый пароль - это 64 символа от арифметической последовательности, причем первый член равен 1, разность прогрессии равна 5.:\n')
            for idx, password in enumerate(passwords, start=1):
                file.write(f'Password with arithmetic progression {idx}: {password}\n')
        
        QMessageBox.information(self, 'Уведомление', 'Пароли успешно записаны.')


    # геометрическая прогрессия
    def generate_sequence(self, start, ratio, n):
        return [start * ratio ** i for i in range(n)]

    def generate_passwords_with_geometric_progression(self, max_length=64):
        number_passwords = self.spin_box.value()

        if count < 1:
            QMessageBox.information(self, "Уведомление", "Количество паролей должно быть не менее 1.")
            return

        start = 2
        ratio = 3
        count = 500
        sequence = self.generate_sequence(start, ratio, count)
        sequence_string = ''.join(str(num) for num in sequence)
        passwords = [sequence_string[i:i + max_length] for i in range(0, len(sequence_string), max_length)]
        passwords = passwords[:number_passwords]
                
        with open('geometric_progression_passwords.txt', 'w') as file:
            file.write('Каждый новый пароль - это 64 символа геометричекой прогрессии, '
                       'причем начало 2, знаменатель прогрессии 3, степень определяется от 1 с шагом 1:\n')
            for idx, password in enumerate(passwords, start=1):
                file.write(f"Password with geometric progression {idx}: {password}\n")
        
        QMessageBox.information(self, 'Уведомление', 'Пароли успешно записаны.')


  

    # добавление констант
    def prompt_for_constant(self):
        dialog = QDialog(self)
        dialog.setWindowTitle('Введите константу')
        layout = QVBoxLayout()

        const_input = QLineEdit(dialog)
        const_input.setValidator(QDoubleValidator())  # Ограничение ввода только числами

        confirm_button = QPushButton("ОК", dialog)
        confirm_button.clicked.connect(lambda: self.generate_passwords_with_constant_addition(const_input.text(), dialog))

        layout.addWidget(QLabel('Введите значение константы:'))
        layout.addWidget(const_input)
        layout.addWidget(confirm_button)

        dialog.setLayout(layout)
        dialog.exec_()

    def generate_passwords_with_constant_addition(self, constant_value, dialog):
        dialog.accept()
        try:
            const = float(constant_value)
        except ValueError:
            QMessageBox.warning(self, 'Ошибка', 'Пожалуйста, введите допустимое числовое значение для константы.')
            return
        
        count = self.spin_box.value()
        if count < 1:
            QMessageBox.information(self, 'Уведомление', 'Количество паролей должно быть не менее 1.')
            return
        
        start = 2  # Начальное значение
        constant_sequence = self.constant_addition_sequence(start, const, 100000)
        
        # Преобразуем числа последовательности в строку
        const_string = ''.join(str(num) for num in constant_sequence).replace('.', '')
        
        # Генерация паролей, каждый длиной до max_length символов
        max_length = 64
        passwords = [const_string[i:i + max_length] for i in range(0, len(const_string), max_length)]
        
        # Обрезаем список паролей до указанного количества
        passwords = passwords[:count]
        
        # Записываем пароли в файл
        with open('constant_addition_passwords.txt', 'w') as file:
            file.write('Каждый новый пароль высчитывается из отношения сложения начального заданного значения и'
                       'номера пароля, возведенного в степень введенного константного значения:\n')
            for idx, password in enumerate(passwords, start=1):
                file.write(f'Password with constant addition {idx}: {password}\n')
        
        QMessageBox.information(self, 'Уведомление', 'Пароли успешно записаны.')

    def constant_addition_sequence(self, start, const, n):
        return [start + i * const for i in range(n)]
        



    # числа Каталана
    def catalan_number(self, n):
        if n <= 1:
            return 1
        catalan = [0] * (n + 1)
        catalan[0] = catalan[1] = 1

        for i in range(2, n + 1):
            catalan[i] = sum(catalan[j] * catalan[i - j - 1] for j in range(i))
        return catalan[n]

    def generate_passwords_with_catalan_numbers(self, max_length=64):
        count = self.spin_box.value()

        # Генерация последовательности чисел Каталана
        catalan_sequence = [self.catalan_number(i) for i in range(1, 500)]
        
        # Преобразуем числа Каталана в строку и убираем точки
        catalan_string = ''.join(str(num) for num in catalan_sequence).replace('.', '')
        
        # Генерация паролей, каждый длиной до max_length символов
        passwords = [catalan_string[i:i + max_length] for i in range(0, len(catalan_string), max_length)]

        passwords = passwords[:count]
        
        # Записываем пароли в файл
        with open('numbers_catalan_passwords.txt', 'w') as file:
            file.write(f'Числа Каталана — последовательность, в которой n-ное число выражается формулой C(n) = (2n)!/ (n! (n+1)!).'
                       'Каждый новый пароль - это 64 символа от этой последовательности.\n')
            for idx, password in enumerate(passwords, start=1):
                file.write(f"Password with numbers catalan {idx}: {password}\n")
        
        QMessageBox.information(self, 'Уведомление', 'Пароли успешно записаны.')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())
