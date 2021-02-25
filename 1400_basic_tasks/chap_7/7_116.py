from main_funcs import get_input


def mean_series(n:int, cond:Union[int, float]=5000) -> bool:
    tot_car = 0
    tot_bike = 0
    num_car = 0
    num_bike = 0
    
    for _ in range(n):
        a = get_input('Укажите стоимость ТС: ')
        
        if a > cond:
            tot_car += a
            num_car += 1
        else:
            tot_bike += a
            num_bike += 1 
    
    
    
    mean_car = tot_car / num_car
    mean_bike = tot_bike / num_bike
    
    return(mean_car / mean_bike > 3)