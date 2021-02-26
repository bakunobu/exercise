from main_funcs import get_input


def take_heith(n:int=20) -> list:
    msg = 'Укажите количество очков: '
    heigth_list = [get_input(msg) for _ in range(n)]
    return(heigth_list.sort(reverse=True))


def add_new_student(table:list) -> int:
    i = 0
    points = get_input('Укажите рост ученика: ')
    while table[i] > points:
        i += 1
        
    return(i)
