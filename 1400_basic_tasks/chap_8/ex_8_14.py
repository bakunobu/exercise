from fractions import Fraction


def find_fist_lesser() -> None:
    
    while True:
        try:
            a = float(input('Введите число: '))
            if 0 < a <= 1:
                break
            else:
                print('Число должно принадлежать интервалу от 0 до 1!')
        except ValueError:
            print('Используйте десятичные дроби с разделителем - .')
    
    i = 1        
    while a >= Fraction(1, i):
        i += 1
        
    print(Fraction(1, i))