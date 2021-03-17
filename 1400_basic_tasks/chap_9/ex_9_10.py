def collect_points(n:int) -> list:
    journal = [[] for i in range(n)]
    for i in range(n):
        msg = f'Введите зарплату {i+1} работника: '
        while True:
            try:
                a, b, c, d, e = [float(x) for x in input(msg).split()]
                break
            except ValueError:
                print('Используйте дробные числа (разделитель - \'.\'')
        journal[i] = [a, b, c, d, e]
    return(journal)


# a
def max_salary(my_list:list) -> float:
    salaries = []
    for score in my_list:
        salaries += score
        
    return(max(salaries))


# b
def max_worker_salary(my_list:list) -> int:
    salaries = [sum(salary) for salary in my_list]
    max_salary = max(salaries)
    return(salaries.index(max_salary))


# c
def best_month(my_list:list) -> int:
    month_1 = [salary[0] for salary in my_list]
    month_2 = [salary[1] for salary in my_list]
    month_3 = [salary[2] for salary in my_list]
    top_salaries = [sum(m) for m in [month_1, month_2, month_3]]
    max_salary = max(top_salaries)
    return(top_salaries.index(max_salary))