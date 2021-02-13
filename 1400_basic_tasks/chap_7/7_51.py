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
                
                
def calc_odd_seq() -> int:
    total = 0
    a = get_input('Введите число: ', False)
    while a % 2 != 0:
        total += a
        a = get_input('Введите число: ', False)
    return(total)

print(calc_odd_seq())