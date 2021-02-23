from main_funcs import get_input


def change_sign(n:int) -> int:
    change_counter = 0
    prev_a = get_input('Введите число: ', False)
    for x in range(n-1):
        a = get_input('Введите число: ', False)
        if a * prev_a < 0:
            change_counter += 1
        prev_a = a
    return(change_counter)

