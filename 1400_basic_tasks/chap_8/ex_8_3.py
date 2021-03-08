from fractions import Fraction


def calc_part() -> None:
    while True:
        try:
            a = float(input('Введите число: '))
            if 0 < a <= 1:
                break
            else:
                print('Число должно принадлежать интервалу от 0 до 1!')
        except ValueError:
            print('используйте десятичные дроби с разделителем - .')
    i = 1
    while Fraction(1 , i) >= a:
        print(Fraction(1, i))
        i += 1
        
        
calc_part()