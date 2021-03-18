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
def min_students(my_list:list) -> int:
    all_classes = []
    for cl in my_list:
        all_classes += cl
    return(min(all_classes))


# b
def min_parallel(my_list:list) -> int:
    tot_per_parall = [sum(cl) for cl in my_list]
    return(min(tot_per_parall))


# c
def min_class(my_list:list) -> int:
    a_par = sum([cl[0] for cl in my_list])
    b_par = sum([cl[1] for cl in my_list])
    c_par = sum([cl[2] for cl in my_list])
    d_par = sum([cl[3] for cl in my_list])
    return(min(a_par, b_par, c_par, d_par))
                