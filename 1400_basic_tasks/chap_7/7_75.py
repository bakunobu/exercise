from main_funcs import get_input
import math
import scipy.constants as const


# Что это все значит?
# нам нужно найти время t, зная координату x
# потом определить, попадает ли координата y в интервал [H, P]

# функция получения времени
def get_t(v_0:float, alpha:float, R:float) -> float:
    expr = v_0 * math.cos(alpha)
    return(R / expr)

# получение координаты y
def calc_y_cord(v_0:float, alpha:float, t:float) -> float:
    expr_1 = v_0 * math.sin(alpha)
    expr_2 = (const.g * t ** 2) / 2
    return(expr_1 - expr_2)


# основная функция
def calc_accuracy(n: int, R:float,
                  H: float, P: float) -> float:
    on_goal = 0
    for _ in range(n):
        v_0 = get_input('Укажите начальную скорость: ')
        alpha = get_input('Укажите угол вылета снаряда: ')
        t = get_t(v_0, alpha, R)
        y_cord = calc_y_cord(v_0, alpha, t)
        if H <= y_cord <= P:
            on_goal += 1   
    return(round(on_goal / n, 5))

print(calc_accuracy(5, 100.0, 1.0, 1.0))