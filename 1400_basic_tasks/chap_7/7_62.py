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
def bigger_than_p(n:int, p:Union[int, float]) -> int:
    msg = 'Введите число: '
    nums = [1 if get_input(msg, False) > p else 0 for _ in range(n)]
    return(sum(nums))


# b
def ends_wiht_q(n:int, q:int=5) -> int:
    msg = 'Введите число: '
    nums = [1 if get_input(msg, False) % 10 == 5 else 0 for _ in range(n)]
    return(sum(nums))


# c
def divs_by_k(n:int, k:int) -> int:
    msg = 'Введите число: '
    nums = [1 if get_input(msg, False) % k == 0 else 0 for _ in range(n)]
    return(sum(nums))