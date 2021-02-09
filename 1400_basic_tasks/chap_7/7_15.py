def give_num() -> float:
    while True:
        try:
            a = float(input('Введите число: '))
            return(a)
        except ValueError:
            print('Используйте только числа (разделитель - \'.\')')


def is_sum_bigger(n:int=10, lim:float=100.78) -> bool:
    total = 0
    for x in range(n):
        i = give_num()
        total += i
    return(total <= lim)

