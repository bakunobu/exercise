from main_funcs import get_input

# a
def last_max_people(n:int) -> int:
    ind = 1
    max_num = get_input('Укажите количество жильцов: ', False)
    for i in range(2, n+1):
        a = get_input('Укажите количество жильцов: ', False)
        if a >= max_num:
            ind = i
    return(ind)
