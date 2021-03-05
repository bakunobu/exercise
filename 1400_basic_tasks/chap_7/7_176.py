from main_funcs import get_input


def two_cold_days(d:int=31) -> tuple:
    cold_ind = 0
    sec_cold_ind = 0
    low_temp = False
    sec_low_temp = False
    
    for i in range(d):
        t = get_input('Укажите температуру: ')
        
        if not low_temp:
            low_temp = t
        elif not sec_cold_ind:
            sec_low_temp = t
        else:
            if low_temp < t:
                sec_low_temp = low_temp
                sec_cold_ind = cold_ind
                low_temp = t
                cold_ind = i
            elif sec_low_temp < t:
                sec_low_temp = t
                sec_cold_ind = i
    
    return(cold_ind, sec_cold_ind)