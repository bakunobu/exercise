from main_funcs import get_input


def calc_el_cur(R:float, U:float) -> float:
    return(U / R)


def find_max_el_cur(n:int=20) -> int:
    max_el = 0
    max_ind = 0
    
    for i in range(n):
        r = get_input('Укажите сопротивление проводника: ')
        u = get_input('Укажите напряжение для проводника: ')
        el = calc_el_cur(r, u)
        if el > max_el:
            max_el = el
            max_ind = i
    
    return(max_ind)