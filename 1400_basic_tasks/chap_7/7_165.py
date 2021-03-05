from main_funcs import get_input


def get_speed(s:float, t:float) -> float:
    return(s * t)


def calc_max_speed(n:int=25) -> int:
    max_speed = 0
    ind = 0
    
    for i in range(n):
        s = get_input('Укажите пройденное расстояние: ')
        t = get_input('Укажите затраченное время: ')
        v = get_speed(s, t)
        
        if max_speed < v:
            max_speed = v
            ind = i
            
    return(ind)