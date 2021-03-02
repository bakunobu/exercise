def calc_density(m:float, v:float) -> float:
    return(m / v)


def calc_max_dense(n:int=20) -> float:
    max_dense = 0
    msg = 'Укажите массу и объем вещества (через пробел)'
    for _ in range(n):
        try:
            m, v = [float(x) for x in input(msg).split( )]
        except ValueError:
            print('Используйте вещественные числа и пробел для их разделения')
        dense = calc_density(m, v)
        if dense > max_dense:
            max_dense = dense
    return(max_dense)