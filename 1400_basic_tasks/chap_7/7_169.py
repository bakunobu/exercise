from main_funcs import get_input


def session_time(n:int) -> str:
    best_ses = 0
    worth_ses = 0
    best_time = False
    worth_time = False
    
    for i in range(n):
        x = get_input('Введите время прохождения этапа: ', False)
        
        if not best_time:
            best_time = x
            best_ses = i
        if not worth_time:
            worth_time = x
            worth_ses = i
        
        if x < best_time:
            best_time = x
            best_ses = i
            
        elif x > worth_time:
            worth_time = x
            worth_ses = i
    
    if best_ses > worth_ses:
        return('Сначала лучший')
    else:
        return('Сначала худший')