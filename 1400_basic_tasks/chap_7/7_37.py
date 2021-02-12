def return_dense(pop:float, area:float) -> float:
    return(pop / area)


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


def calc_reg_area(n:int=12) -> float:
    tot_pop = 0
    tot_area = 0
    for i in range(n):
        mes_1 = 'укажите население {}-го района: '.format(i+1)
        mes_2 = 'укажите площадь {}-го района: '.format(i+1)
        pop = get_input(mes_1)
        area = get_input(mes_2)
        tot_pop += pop
        tot_area += area
    return(return_dense(tot_pop, tot_area))
    