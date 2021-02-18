from main_funcs import get_input


def calc_penalties() -> tuple:
    num_dict = {1:0, 2:0}
    time_dict = {1:0, 2:0}
    msg = 'Укажите команду и длительность удаления (разделитель - пробел): '
    data = ''
    while True:
        data = input(msg)
        if data == '0':
            break
        else:
            try:
                team, time = [int(x) for x in data.split(' ')]
                num_dict[team] += 1
                time_dict[team] += time
                
            except ValueError:
                print('Используйте целые числа!')

    return((num_dict[1], time_dict[1]),
           (num_dict[2], time_dict[2]))
    
    
print(calc_penalties())