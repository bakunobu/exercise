from typing import Union


def calc_points() -> list:
    prog = ('обязательную', 'короткую', 'произвольную')
    journal = [[] for i in range(12)]
    for i in range(3):
        for j in range(15):
            msg = f'Введите оценку {j+1} работника за {prog[i]} программу: '
            while True:
                try:
                    g = float(input(msg))
                    break
                except ValueError:
                    print('Используйте только десятичные дроби (разделитель -\'.\'!')
            journal[j].append(g)
            
    return(journal)


# a
def calc_mean_points(my_list:list) -> Union[float, int]:
    mean_list = [sum(x) / 3 for x in my_list]
    return(sum(mean_list))


# c
def calc_mean_per_prog(my_list:list) -> tuple:
    month_1 = sum([x[0] for x in my_list])
    month_2 = sum([x[1] for x in my_list])
    month_3 = sum([x[0] for x in my_list])
    return(month_1 / 15, month_2 / 15, month_3 / 15)