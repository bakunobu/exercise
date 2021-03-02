from main_funcs import get_input

def calc_interval(n:int) -> float:
    msg = 'Укажите рост ученика: '
    heigth_table = [get_input(msg) for x in range(n)]
    return(max(heigth_table) - min(heigth_table))