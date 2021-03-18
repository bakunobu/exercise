def collect_salaries(n:int) -> list:
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
def max_salary_per_worker(my_list:list) -> list:
    max_salaries = []
    for worker in my_list:
        max_salary = max(worker)
        max_salaries.append(worker.index(max_salary))
        
    return(max_salaries)


# b
def max_salary_per_month(my_list:list) -> list:
    max_salaries_month = []
    salaries_month_1 = [month[0] for month in my_list]
    salaries_month_2 = [month[1] for month in my_list]
    salaries_month_3 = [month[2] for month in my_list]
    for month in (salaries_month_1,
                  salaries_month_2,
                  salaries_month_3):
        max_salary = max(month)
        max_salaries_month.append(month.index(max_salary))
    
    return(max_salaries_month)