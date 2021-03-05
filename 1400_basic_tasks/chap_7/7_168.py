from main_funcs import get_input


def which_earlier(n:int) -> str:
    max_ind = 0
    min_ind = 0
    max_num = False
    min_num = False
    
    for i in range(n):
        x = get_input('Введите возраст: ', False)
        
        if not max_num:
            max_num = x
            max_ind = i
        if not min_num:
            min_num = x
            min_ind = i
        
        if x > max_num:
            max_num = x
            max_ind = i
            
        elif x < min_num:
            min_num = x
            min_ind = i
    
    if max_ind > min_ind:
        return('Сначала старший')
    else:
        return('Сначала младший')
    