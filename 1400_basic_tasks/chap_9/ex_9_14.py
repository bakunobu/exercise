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
def max_revenue(my_list:list) -> int:
    revenue = [sum(shop) for shop in my_list]
    max_rev = max(revenue)
    return(revenue.index(max_rev))


# b
def revenue_per_day(my_list:list) -> int:
    day_rev = []
    for i in range(10):
        day = sum(my_list[0][i],
                  my_list[1][i],
                  my_list[2][i])
        day_rev.append(day)
    max_rev = max(day_rev)
    return(day_rev.index(max_rev))


# c
def max_rev_per_store(my_list:list) -> tuple:
    rev_dict = {}
    i = 0
    for shop in my_list:
        max_rev = max(shop)
        max_rev_day = shop.index(max_rev)
        rev_dict[max_rev] = (i+1, max_rev_day)
        i += 1
    maximum_rev = max(list(rev_dict.keys()))
    return(rev_dict.get(maximum_rev, tuple(0, 0)))
    