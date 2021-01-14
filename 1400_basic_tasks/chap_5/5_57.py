import scipy.integrate as integrate


def calc_eq(x:float) -> float:
    return(0.3 * (x - 1) ** 2 + 3)


def calc_area(my_func, x_1:float, x_2:float) -> float:
    area = integrate.quad(my_func, x_1, x_2)[0]
    return(area)


S = calc_area(calc_eq, 2, 4)
print(S)

