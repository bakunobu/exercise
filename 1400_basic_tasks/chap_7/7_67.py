from main_funcs import get_input


def before_zero() -> int:
    counter = 0
    while True:
        a = get_input('Введите число: ')
        if a == 0.0:
            break
        counter += 1
    return(counter)