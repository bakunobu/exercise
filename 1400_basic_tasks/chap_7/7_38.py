def return_area(pop:float, dens:float) -> float:
    return(pop / dens)


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
    tot_area = 0
    for i in range(n):
        mes_1 = 'укажите население {}-го района: '.format(i+1)
        mes_2 = 'укажите плотность населения {}-го района: '.format(i+1)
        pop = get_input(mes_1)
        dens = get_input(mes_2)
        tot_area += return_area(pop, dens)
    return(tot_area)
    