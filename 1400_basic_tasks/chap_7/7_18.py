from typing import Union


def give_num(text:str='Введите число: ', is_int:bool=False) -> Union[int, float]:
    if is_int:
        while True:
            try:
                a = int(input(text))
                return(a)
            except ValueError:
                print('Используйте только числа (разделитель - \'.\')')

    else:
        while True:
            try:
                a = float(input(text))
                return(a)
            except ValueError:
                print('Используйте только числа (разделитель - \'.\')')


def is_sum_divisible(n:int, div:int) -> bool:
    total = 0
    for x in range(n):
        i = give_num()
        total += i
    return(not total % div)


def give_params() -> tuple:
    n = give_num('Укажите длину последовательности: ', True)
    b = give_num('Укажите делитель: ', True)
    return(is_sum_divisible(n, b))


print(give_params())