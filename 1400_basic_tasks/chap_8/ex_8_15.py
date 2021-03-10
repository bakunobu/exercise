def seq_qunc(x:int) -> float:
    num = x ** 2 + 100
    den = x + 200
    return(num / den)

def calc_less_nums(my_func,
                   min_value:float, max_value:float) -> None:
    while True:
        try:
            m = float(input('Введите число: '))
            if min_value <= m <= max_value:
                break
            else:
                print(f'Число должно быть в интервале {min_value}:{max_value}.')
        except ValueError:
            print('Используйте целые числа и десятичные дроби!')
    i = 1
    while my_func(i) < m:
        print(my_func(i))
        i += 1
        
        
calc_less_nums(seq_qunc, 0.52, 33.7)
            