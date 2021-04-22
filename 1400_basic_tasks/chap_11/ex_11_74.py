def float_input(msg) -> float:
    while 1:
        try:
            a = float(input(msg))
            return(a)
        except ValueError:
            print('Используйте числа с плавающей точкой!')
            

def nums_in_interval(nums:list, a:float, b:float) -> list:
    return([x for x in nums if a < x < b])   
    
            
def interval_nums(nums:list) -> list:
    msg_min = 'Введите меньшее число: '
    a = float_input(msg_min)
    msg_max = 'Введите большее число: '
    b = float_input(msg_max)
    return(nums_in_interval(nums, a , b))