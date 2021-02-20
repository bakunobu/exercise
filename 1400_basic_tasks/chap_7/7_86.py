from main_funcs import get_input


def cond_num_counter(n:int, lim:int=20, p:int=5) -> bool:
    num_count = 0
    for _ in range(n):        
        c = get_input('Введите число: ', False)
        if c < lim:
            num_count += 1
            if num_count > 5:
                break
    return(num_count == 5)