from main_funcs import get_input


# a
def calc_base_pairs(n:int) -> int:
    pairs = 0
    a_i = get_input('Введите число', False)
    for _ in range(n):
        a = get_input('Введите число', False)
        if a_i == a:
            pairs += 1
        else:
            a_i = a
    return(pairs)


# b
def calc_zero_pairs(n:int) -> int:
    pairs = 0
    a_i = get_input('Введите число', False)
    for _ in range(n):
        a = get_input('Введите число', False)
        if a_i == a and a == 0:
            pairs += 1
        else:
            a_i = a
    return(pairs)


# c
def calc_even_pairs(n:int) -> int:
    pairs = 0
    a_i = get_input('Введите число', False)
    for _ in range(n):
        a = get_input('Введите число', False)
        if a_i == a and a % 2 == 0:
            pairs += 1
        else:
            a_i = a
    return(pairs)


# d
def calc_end_five_pairs(n:int) -> int:
    pairs = 0
    a_i = get_input('Введите число', False)
    for _ in range(n):
        a = get_input('Введите число', False)
        if a_i == a and a % 10 == 5:
            pairs += 1
        else:
            a_i = a
    return(pairs)
