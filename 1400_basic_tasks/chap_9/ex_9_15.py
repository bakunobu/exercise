def collect_rev(n:int=3, d:int=10) -> list:
    journal = []
    for i in range(n):
        shop = []
        for j in range(d):
            msg = f'Введите доход {i+1} магазина за {j+1} день: '
            while True:
                try:
                    r = float(input(msg))
                    break
                except ValueError:
                        print('Используйте дробные числа (разделитель - \'.\'')
            shop.append(r)
        journal.append(shop)
    return(journal)


# a
def get_max_rev_date(my_list:list) -> int:
    max_rev = max(my_list)
    return(my_list.index(max_rev) + 1)


def max_revenue(my_list:list) -> tuple:
    max_rev = tuple(get_max_rev_date(shop) for shop in my_list)
    return(max_rev)


# b
def rotate_list(my_list:list) -> list:
    i, j = len(my_list), len(my_list[0])
    cal_list = [[] for _ in range(j)]
    for m in range(j):
        for n in range(i):
            cal_list[m].append(my_list[n][m])
    
    return(cal_list)


def get_max_rev_date(my_list:list) -> int:
    max_rev = max(my_list)
    return(my_list.index(max_rev) + 1)


def max_revenue(my_list:list) -> tuple:
    max_rev = tuple(get_max_rev_date(date) for date in my_list)
    return(max_rev)