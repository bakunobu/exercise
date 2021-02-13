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
def calc_abs(a:Union[int,float]) -> Union[int,float]:
    if a < 0:
        return(a * (-1))
    else:
        return(a)
    
def calc_abs_series(n:int) -> Union[int,float]:
    abs_sum = 0
    for i in range(n):
        a = get_input('Введите число: ')
        abs_sum += calc_abs(a)
    return(abs_sum)


# b
def calc_abs_prod(n:int) -> Union[int,float]:
    abs_prod = 1
    for i in range(n):
        a = get_input('Введите число: ')
        abs_prod *= calc_abs(a)
    return(abs_prod)


# c
def calc_pair_sum(n:int) -> list:
    temp_list = [get_input('Введите число: ') for x in range(n)]
    sum_list = [temp_list[i] + temp_list[i+1] for i in range(len(temp_list)-1)]
    return(sum_list)


# d
def calc_neg_prog(n:int) -> Union[int, float]:
    mult = 1
    my_sum = 0
    for i in range(n):
        a = get_input('Введите число: ')
        a *= mult
        mult *= -1
        my_sum += 1
    return(my_sum)