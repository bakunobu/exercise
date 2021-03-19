def collect_studs(n:int=5, d:int=6) -> list:
    journal = []
    for i in range(n):
        year = []
        for j in range(d):
            msg = f'Укажите число студентов {j+1} группы {i+1} курса: '
            while True:
                try:
                    s = int(input(msg))
                    break
                except ValueError:
                        print('Используйте целые числа!')
            year.append(s)
        journal.append(year)
    return(journal)


# a
def studs_per_year(my_list:list) -> int:
    years = [sum(year) for year in my_list]
    min_year = min(years)
    return(years.index(min_year))


# b
def smallest_group(my_list:list) -> tuple:
    min_studs = None
    index = (0, 0)
    for i in range(len(my_list)):
        for j in range(len(my_list[0])):
            if not min_studs:
                min_studs = my_list[i][j]
                index = (i+1, j+1)
            else:
                if min_studs > my_list[i][j]:
                    min_studs = my_list[i][j]
                    index = (i+1, j+1)
    return(index)