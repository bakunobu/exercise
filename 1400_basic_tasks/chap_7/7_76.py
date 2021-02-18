from main_funcs import get_input


def calc_penalties(n:int=24) -> tuple:
    num_dict = {1:0, 2:0}
    time_dict = {1:0, 2:0}
    msg = 'Укажите команду и длительность удаления (разделитель - пробел): '
    for _ in range(n):
        while True:
            try:
                team, time = [int(x) for x in input(msg).split(' ')]
                num_dict[team] += 1
                time_dict[team] += time
                break
            except ValueError:
                print('Используйте целые числа!')
    return((num_dict[1], time_dict[1]),
           (num_dict[2], time_dict[2]))
    