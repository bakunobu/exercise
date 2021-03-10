from fractions import Fraction


def print_parts() -> None:
    while True:
        try:
            m = float(input('Введите число: '))
            if 0.5 < m < 1:
                break
            else:
                print(f'Число должно принадлежать отрезку (0.5; 1).')
        except ValueError:
            print('Используйте целые числа и десятичные дроби!')
    i = 1
    while Fraction(i, i+1) < m:
        print(i / (i+1))
        i += 1
        
print_parts()