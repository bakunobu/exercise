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
    
                
def calc_sum(n:int=15) -> int:
    my_sum = 0
    for i in range(n):
        d = get_input('Введите число: ', False)
        if i % 2 == 0:
            my_sum -= d
    return(my_sum)