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
                
                
def calc_price(n:int, d:float=1000.0) -> float:
    total = 0
    for x in range(n):
        a = get_input('Укажите цену товара: ')
        if a >= d:
            total += a
    return(total)