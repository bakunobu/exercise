from main_funcs import get_input


def num_neg(n:int, x:int) -> bool:
    num_count = 0
    for _ in range(n):
        a = get_input('Введите число: ', False)
        if a <= 0:
            num_count += 1
    return(num_count == x)