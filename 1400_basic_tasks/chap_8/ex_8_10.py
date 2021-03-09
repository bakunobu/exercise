"""
Упражнение сломанное, так как получим бесконечно убывающую последовательность c lim=1.
Можно предположить, что есть некоторое n, обозначающее нижнюю границу (знеменатель дроби).
Тогда задание имеет смысл.
"""

from fractions import Fraction


def calc_part(n:int=100) -> None:
    
    while True:
        try:
            a = float(input('Введите число: '))
            if 1 < a <= 1.5:
                break
            else:
                print('Число должно принадлежать интервалу от 1 до 1.5!')
        except ValueError:
            print('Используйте десятичные дроби с разделителем - .')
    
    for i in range(1, n+1):
        if Fraction(1 , i) + 1 < a:
            print(1, end='+')
            print(Fraction(1, i))
                
        
calc_part()