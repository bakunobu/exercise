from main_funcs import get_input


def calc_mean(n:int) -> tuple:
    i = 0
    j = 0
    fat_sum = 0
    slim_sum = 0
    for _ in range(n):
        a = get_input('Введите массу: ',)
        if a > 100:
            i += 1
            fat_sum += a
        else:
            j += 1
            slim_sum += a
    return(odd_sum / i, even_sum / j)
        