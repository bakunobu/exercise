from main_funcs import get_input


def equal_seq(n: int) -> int:
    a = get_input('Введите число: ', False)
    b = get_input('Введите число: ', False)
    i = 0
    counter = 0
    while a == b and i < n:
        i += 1
        b = get_input('Введите число: ', False)
        counter += 1
    
    return(counter)