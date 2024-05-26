'''
Используемые библиотеки
'''

from decimal import Decimal, getcontext
import math

'''
Функции
'''
def sqrt_with_precision(get_number, precision=64):
    # Устанавливаем уровень точности
    getcontext().prec = precision - 1 # Добавляем дополнительные цифры для точности в расчетах
    
    return str(Decimal(get_number).sqrt())


'''
Приложение
'''

