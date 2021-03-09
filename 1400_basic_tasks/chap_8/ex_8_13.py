from fractions import Fraction


def calc_part_sum() -> None:
    
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
    i = 1
    while total < a:
        total += Fraction(1, i)
        i += 1
    print(i)
    
        
calc_part_sum()