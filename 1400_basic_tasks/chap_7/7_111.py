from main_funcs import get_input


def class_heith(n:int) -> tuple:
    boys_heith = 0
    tot_boys = 0
    girls_heith = 0
    tot_girls = 0
    for _ in range(n):
        a = get_input('Укажите рост ученика: ')
        if a > 0:
            girls_heith += a
            tot_girls += 1
        else:
            boys_heith += (-1 * a)
            tot_boys += 1
    return(boys_heith / tot_boys,
           girls_heith / tot_girls)