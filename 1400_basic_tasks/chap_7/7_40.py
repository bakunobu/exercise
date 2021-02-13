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
    
                
def calc_sum(n:int, lim:float=10.75) -> float:
    my_sum = 0
    for i in range(n):
        a = get_input('Введите число: ')
        if a > lim:
            my_sum += a
    return(my_sum)

