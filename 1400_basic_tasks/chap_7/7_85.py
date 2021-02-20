from main_funcs import get_input


def num_is_div_by_four(n:int, p:float=32.5) -> bool:
    num_count = 0
    for _ in range(n):
        a = get_input('Введите число: ')
        if a <= p:
            num_count += 1
    return(not num_count % 4)