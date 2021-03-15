from typing import Union


# a
def collect_grades() -> list:
    journal = [[] for i in range(12)]
    for i in range(12):
        msg = f'Введите оценки {i+1} ученика: '
        while True:
            try:
                a, b, c = [int(x) for x in input(msg).split()]
                break
            except ValueError:
                print('Используйте целые числа')
        journal[i] = [a, b, c,]
    return(journal)


def calc_total(my_list:list) -> Union[float, int]:
    sum_list = [sum(x) for x in my_list]
    return(sum(sum_list))
 
                   
# b
def collect_grades() -> list:
    journal = [[] for i in range(12)]
    for i in range(3):
        for j in range(12):
            msg = f'Введите оценки {j+1} ученика по {i+1} предмету: '
            while True:
                try:
                    g = int(input(msg))
                    break
                except ValueError:
                    print('Используйте только целые числа!')
            journal[j].append(g)
            
    return(journal)


def calc_total(my_list:list) -> Union[float, int]:
    sum_list = [sum(x) for x in my_list]
    return(sum(sum_list))
