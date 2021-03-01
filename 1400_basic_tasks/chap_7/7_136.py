from main_funcs import get_input


def res_to_sec(res:tuple) -> float:
    total_time = res[0] * 3600 + res[1] * 60 + res[2]
    return(total_time)


def sec_to_res(cur_time:float) -> tuple:
    h = cur_time // 3600
    cur_time %= 3600
    m = cur_time // 60
    s = cur_time % 60
    return(h, m, s)



def print_best_result(n:int) -> None:
    
    try:
        raw_res = input('Введите результат участника (ч м с): ').split(' ')
        h, m, s = int(raw_res[0]), int(raw_res[1]), float(raw_res[2])
    except ValueError:
        print('Используйте прбел в качестве разделителя!')
    
    best_time = res_to_sec(h, m, s)
    print(f'Лучшее время: {h} часов {m} минут {s} сек')
    
    for _ in range(1, n):
        
        try:
            raw_res = input('Введите результат участника (ч м с): ').split(' ')
            h, m, s = int(raw_res[0]), int(raw_res[1]), float(raw_res[2])
        except ValueError:
            print('Используйте прбел в качестве разделителя!')
        
        if best_time < res_to_sec(h, m, s):
            best_time = res_to_sec(h, m, s)
        else:
            h, m, s = sec_to_res(best_time)
        
    print(f'Лучшее время: {h} часов {m} минут {s} сек')
            

    
            
        
    
    