from typing import Union


def get_input(message:str, is_float:bool=True) -> Union[int, float]:
    if is_float:
        while True:
            try:
                a = float(input(message))
                return(a)
            except ValueError:
                print('Используйте только числа (разделитель - \'.\')')
    else:
        while True:
            try:
                a = int(input(message))
                return(a)
            except ValueError:
                print('Используйте только целые числа')
                
                
# a
def count_nums(n:int=14, s:int=100) -> bool:
    my_sum = 0
    for _ in range(n):
        a = get_input('Введите число: ', False)
        if a > 20:
            my_sum += a
    return(my_sum > s)


# b
def count_even(n:int=14) -> bool:
    my_sum = 0
    for _ in range(n):
        a = get_input('Введите число: ', False)
        if a < 50:
            my_sum += a
    return(not my_sum % 2)
    