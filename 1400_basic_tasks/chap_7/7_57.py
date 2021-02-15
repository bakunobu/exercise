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
                
                
def feb_moist(days:int=28, is_leap:bool=False) -> bool:
    d = days
    if is_leap:
        d += 1
    odd_fall, even_fall = 0, 0
    for i in range(d):
        moist = get_input('Укажите количество осадков: ')
        if not i % 2:
            odd_fall += moist
        else:
            even_fall += moist
    
    return(even_fall > odd_fall)


