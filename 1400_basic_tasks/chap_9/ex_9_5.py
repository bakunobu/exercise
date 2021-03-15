from typing import Union


def collect_salary() -> list:
    journal = [[] for i in range(12)]
    for i in range(3):
        for j in range(12):
            msg = f'Введите зарплату {j+1} работника за {i+1} месяц: '
            while True:
                try:
                    g = float(input(msg))
                    break
                except ValueError:
                    print('Используйте только десятичные дроби (разделитель -\'.\'!')
            journal[j].append(g)
            
    return(journal)


# a
def calc_total(my_list:list) -> Union[float, int]:
    sum_list = [sum(x) for x in my_list]
    return(sum(sum_list))


# b
def calc_ones_salary(my_list:list) -> Union[float, int]:
    sum_list = [sum(x) for x in my_list]
    return(sum_list)


# c
def calc_salary_per_month(my_list:list) -> tuple:
    month_1 = sum([x[0] for x in my_list])
    month_2 = sum([x[1] for x in my_list])
    month_3 = sum([x[0] for x in my_list])
    return(month_1, month_2, month_3)