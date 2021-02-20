from main_funcs import get_input


def calc_grades(n:int=12, e:int=3) -> bool:
    g = ''
    i = 0
    while g != e and i < 12:
        g = get_input('Введите оценку: ', False)
        i += 1

    return(not g == e)

