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
                
                
def month_pos_temp(d:int) -> int:
    counter = 0
    for x in range(d):
        temp = get_input('Укажите температуру: ')
        if temp < 0:
            counter += 1
    return(counter)