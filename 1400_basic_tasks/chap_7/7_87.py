from main_funcs import get_input


def num_div_three(m:int, lim:int=0, p:int=3) -> bool:
    num_count = 0
    for _ in range(m):
        d = get_input('Введите число: ', False)
        if d >= 0:
            num_count += 1
    return(not num_count % p)