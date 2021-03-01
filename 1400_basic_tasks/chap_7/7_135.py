from main_funcs import get_input


# a
def max_num(n:int) -> float:
    n_max = get_input('Введите число: ')
    for _ in range(1, n):
        x = get_input('Введите число: ')
        if x > n_max:
            n_max = x
    return(n_max)


# b
def min_num(n:int) -> float:
    n_min = get_input('Введите число: ')
    for _ in range(1, n):
        x = get_input('Введите число: ')
        if x < n_min:
            n_min = x
    return(n_min)

# c
def min_max_num(n:int) -> tuple:
    n_max = get_input('Введите число: ')
    n_min = n_max
    for _ in range(1, n):
        x = get_input('Введите число: ')
        n_max, n_min = max(x, n_max), min(x, n_min)
    return(n_max, n_min)