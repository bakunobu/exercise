def collect_studs(n:int=11) -> list:
    journal = [[] for i in range(n)]
    for i in range(n):
        msg = f'Введите количество учеников в классах {i+1} параллели: '
        while True:
            try:
                a, b, c, d, = [int(x) for x in input(msg).split()]
                break
            except ValueError:
                print('Используйте целые числа!')
        journal[i] = [a, b, c, d,]
    return(journal)


# a
def min_studs_per_par(my_list:list) -> list:
    min_studs = [min(cl) for cl in my_list]
    return(min_studs)


# b
def min_studs_per_class(my_list:list) -> list:
    a_par = [cl[0] for cl in my_list]
    b_par = [cl[1] for cl in my_list]
    c_par = [cl[2] for cl in my_list]
    d_par = [cl[3] for cl in my_list]
    return(min(a_par), min(b_par),
           min(c_par), min(d_par))

