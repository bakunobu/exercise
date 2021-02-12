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


# *a
def calc_sum(n:int) -> int:
    temp_list = [get_input('Введите число: ', False) for x in range(n)]
    return(temp_list[0] + temp_list[-1])


# b
def calc_diff(n:int) -> int:
    temp_list = [get_input('Введите число: ', False) for x in range(n)]
    return(temp_list[1] - temp_list[-2])

