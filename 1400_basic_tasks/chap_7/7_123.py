from main_funcs import get_input


def take_heith(n:int=15) -> list:
    msg = 'Укажите рост ученика: '
    heigth_list = [get_input(msg) for _ in range(n)]
    return(heigth_list.sort(reverse=True))


def add_new_student(height:list) -> int:
    i = 0
    new_stud = get_input('Укажите рост ученика: ')
    h = height[i]
    while h > new_stud:
        i += 1
        h = height[i]
    return(i)

