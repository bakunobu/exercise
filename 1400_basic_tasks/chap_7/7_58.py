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
                
                
def street_pop(n:int) -> bool:
    odd_pop, even_pop = 0, 0
    for i in range(n):
        pop = get_input('Укажите число жильцов: ', False)
        if not i % 2:
            odd_pop += pop
        else:
            even_pop += pop
    
    return(even_pop > odd_pop)


def printer(is_even:bool) -> str:
    if is_even:
        print('В дома с четными номерами проживает больше жителей')
    else:
        print('В домах с нечетными номерами проживает больше жителей')