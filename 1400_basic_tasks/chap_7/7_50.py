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
                
                
def calc_pupils(n:int=1) -> float:
    total_pupils = 0
    i = 0
    for x in range(n):
        a = get_input('Укажите число учеников: ', False)
        if i % 2 == 0:
            total_pupils += a
        i += 1
    return(total_pupils)