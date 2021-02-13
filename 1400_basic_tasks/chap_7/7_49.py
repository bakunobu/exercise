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
                
                
def calc_moist(n:int=30) -> float:
    total_fall = 0
    i = 0
    for x in range(n):
        a = get_input('Укажите количество осадков: ')
        if i % 2 != 0:
            total_fall += a
        i += 1
    return(total_fall)