from main_funcs import get_input


def num_div_p(n:int, m:int, p:int) -> bool:
    num_count = 0
    for _ in range(n):
        a = get_input('Введите число: ', False)
        if d >= m:
            num_count += 1
    return(not num_count % p)