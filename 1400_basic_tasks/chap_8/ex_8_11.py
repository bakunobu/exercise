import fractions
from fractions import Fraction



def calc_part_sum() -> fractions.Fraction:
    
    while True:
        try:
            n = float(input('Введите число: '))
            if n >= 1:
                break
            else:
                print('Число должно быть не меньше единицы!')
        except ValueError:
            print('Используйте десятичные дроби с разделителем - .')
    
    total = 0
    i = 1
    while total <= n:
        total += Fraction(1, i)
        i += 1
    
    return(total)
        
print(calc_part_sum())