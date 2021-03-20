def collect_goodies(n:int=5, d:int=6) -> list:
    journal = []
    for i in range(n):
        year = []
        for j in range(d):
            msg = f'Укажите стоимость {j+1} товаров в {i+1} день: '
            while True:
                try:
                    s = float(input(msg))
                    break
                except ValueError:
                        print('Используйте целые числа (разделитель - \'.\')!')
            year.append(s)
        journal.append(year)
    return(journal)


# a
def count_per_good(my_list:list) -> list:
    revenue = [sum(good) for good in my_list]
    return(revenue)


# b
def rotate_list(my_list:list) -> list:
    i, j = len(my_list), len(my_list[0])
    cal_list = [[] for _ in range(j)]
    for m in range(j):
        for n in range(i):
            cal_list[m].append(my_list[n][m])
    
    return(cal_list)


def count_per_day(my_list:list) -> list:
    day_list = rotate_list(my_list)
    revenue = [sum(day) for day in day_list]
    return(revenue)


# c
def total_revenue(my_list:list) -> float:
    revenue = count_per_good(my_list)
    return(sum(revenue))


# d
def max_good_rev(my_list:list) -> int:
    revenue = count_per_good(my_list)
    max_rev = max(revenue)
    return(revenue.index(max_rev))


# e
def max_day_revenue(my_list:list) -> int:
    revenue = count_per_day(my_list)
    max_rev = max(revenue)
    return(revenue.index(max_rev))


# f
def greater_than_a(my_list:list, a:float) -> int:
    total_days = 0
    revenue = count_per_day(my_list)
    for rev in revenue:
        if rev > a:
            total_days += 1
    return(total_days)