from typing import Union
from functools import reduce


# a
def list_sum(my_list:list) -> Union[int, float]:
    return(sum(my_list))


# b
def prod_list(my_list:list) -> Union[int, float]:
    return(reduce((lambda x, y: x * y), my_list))


# c
def sum_squares(my_list:list) -> Union[int, float]:
    squares_list = [x ** 2 for x in my_list]
    return(sum(squares_list))


# d
def sum_six_first_els(my_list:list) -> Union[int, float]:
    return(sum(my_list[:6]))


# e
def int_input(msg:str) -> int:
    while 1:
        try:
            k = int(input(msg))
            if k >= 0:
                return(k)
            else:
                print('Используйте неотрицательные числа')
        except ValueError:
            print('Используйте неотрицательные целые числа')
            

k_1 = int_input('Укажите начальный индекс')
k_2 = int_input('Укажите конечный индекс: ')
while k_1 >= k_2:
    print('Конечный индекс должен быть больше начального!')
    k_1 = int_input('Укажите начальный индекс')
    k_2 = int_input('Укажите конечный индекс: ')


def el_ind_sum(my_list:list, start:int, end:int) -> Union[int, float]:
    return(list_sum(my_list[start:end]))


# f
def list_mean(my_list:list) -> float:
    return(sum(my_list) / len(my_list))


# g
s_1 = int_input('Укажите начальный индекс')
s_2 = int_input('Укажите конечный индекс: ')
while s_1 >= s_2:
    print('Конечный индекс должен быть больше начального!')
    s_1 = int_input('Укажите начальный индекс')
    s_2 = int_input('Укажите конечный индекс: ')


def slice_list_mean(my_list:list, start:int, end:int) -> float:
    new_list = my_list[start:end]
    return(list_mean(new_list))    