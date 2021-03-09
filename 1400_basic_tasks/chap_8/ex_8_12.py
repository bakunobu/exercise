"""
Еще одно сломанное упражнение. Без верхнего ограничения для n таких чисел будет бесконечно много!
"""

from fractions import Fraction


def calc_part_sum(n:int=100) -> None:
    
    while True:
        try:
            a = float(input('Введите число: '))
            if a >= 1:
                break
            else:
                print('Число должно быть не меньше единицы!')
        except ValueError:
            print('Используйте десятичные дроби с разделителем - .')
    
    total = 0
    
    for i in range(1, n+1):
        total += Fraction(1, i)
        if total > a:
            print(i)
    
        
calc_part_sum()