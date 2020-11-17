def calc_mean(a:float, b:float) -> float:
    return((a + b) / 2)


def calc_geo_mean(a:float, b:float) -> float:
    return((a * b) ** 0.5)

def show_res(a:float, b:float) -> float:
    print(f'Mean of {a} and {b}: {calc_mean(a, b)}')
    print('Geometric mean of {} and {}: {:.5f}'.format(
        a, b, calc_geo_mean(a, b)))


show_res(1, 2)