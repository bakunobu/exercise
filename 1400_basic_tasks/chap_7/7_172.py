from main_funcs import get_input


def first_second_place(n:int=22) -> tuple:
    first_place = False
    second_place = False
    for i in range(n):
        t = get_input('Введите время спортсмена: ')
        
        if not first_place:
            first_place = t
        elif not second_place:
            second_place = t
        
        else:    
            if first_place <= t:
                second_place = first_place
                first_place = t
            elif second_place < t:
                second_place = t
    
    return(first_place, second_place)
        