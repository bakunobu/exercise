def give_num(text:str='Введите число: ') -> float:
    while True:
        try:
            a = float(input(text))
            return(a)
        except ValueError:
            print('Используйте только числа (разделитель - \'.\')')


def is_sum_bigger(n:int, lim:float) -> bool:
    total = 0
    for x in range(n):
        i = give_num()
        total += i
    return(total <= lim)


def give_params() -> tuple:
    while True:
        try:
            n = int(give_num('Укажите длину последоваельности'))
            break
        except ValueError:
            print('Используйте только целые числа')
    while True:
        try:
            lim = give_num('Укажите ограничение')
        except ValueError:
                print('Используйте только целые числа')
    
    return(is_sum_bigger(n, lim))


print(give_params())
        