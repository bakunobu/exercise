from main_funcs import get_input


def calc_mean(n:int=12) -> tuple:
    i = 0
    j = 0
    odd_sum = 0
    even_sum = 0
    for _ in range(n):
        a = get_input('Введите число: ', False)
        if a % 2:
            i += 1
            odd_sum += a
        else:
            j += 1
            even_sum += a
    return(odd_sum / i, even_sum / j)
        