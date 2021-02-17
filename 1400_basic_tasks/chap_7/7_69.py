from main_funcs import get_input


# a
def calc_grades(grade:int=5) -> int:
    counter = 0
    a = get_input('Введите оценку: ', False)
    while a == grade:
        counter += 1
        a = get_input('Введите оценку: ', False)
    return(counter)


# b
def calc_grades(grade:int=5, n:int=20) -> int:
    counter = 0
    a = get_input('Введите оценку: ', False)
    while a == grade and counter < n:
        counter += 1
        a = get_input('Введите оценку: ', False)
    return(counter)