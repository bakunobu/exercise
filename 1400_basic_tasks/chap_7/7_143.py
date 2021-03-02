def calc_pop_dense(pop:float, area:float) -> float:
    return(pop / area)


def calc_min_pop_dense(n:int=16) -> float:
    min_dense = False
    msg = 'Укажите население и площадь госудаства (через пробел)'
    for _ in range(n):
        try:
            pop, area = [float(x) for x in input(msg).split( )]
        except ValueError:
            print('Используйте вещественные числа и пробел для их разделения')
        dense = calc_min_pop_dense(pop, area)
        if not min_dense:
            min_dense = dense
        if dense < min_dense:
            min_dense = dense
    return(min_dense)