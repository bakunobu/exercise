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
                
                
def sum_is_less(n: int, m:float, q:float) -> bool:
    msg = 'Введите число: '
    total = 0
    
    for _ in range(n):
        a = get_input(msg)
        if a <= m:
            total += a
            
    return(total > q)


print(sum_is_less(5))