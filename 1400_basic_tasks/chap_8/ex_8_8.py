from fractions import Fraction


def calc_part() -> None:
    
    while True:
        try:
            a = float(input('Введите число: '))
            if 1 < a <= 1.5:
                break
            else:
                print('Число должно принадлежать интервалу от 1 до 1.5!')
        except ValueError:
            print('Используйте десятичные дроби с разделителем - .')
    
    i = 1
    
    while Fraction(1 , i) + 1 >= a:
        i += 1
    
        print(i)
    
        
calc_part()