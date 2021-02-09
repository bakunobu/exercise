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


def is_sum_even(n:int) -> bool:
    total = 0
    for x in range(n):
        i = give_num()
        total += i
    return(not total % 2)


def give_param() -> tuple:
    n = give_num('Укажите длину последовательности: ', True)
    return(is_sum_even(n))


print(give_param())