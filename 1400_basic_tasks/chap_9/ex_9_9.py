def collect_points(n:int) -> list:
    journal = [[] for i in range(n)]
    for i in range(n):
        msg = f'Введите баллы {i+1} спортсмена: '
        while True:
            try:
                a, b, c, d, e = [float(x) for x in input(msg).split()]
                break
            except ValueError:
                print('Используйте дробные числа (разделитель - \'.\'')
        journal[i] = [a, b, c, d, e]
    return(journal)


# a
def find_max_points(my_list:list) -> float:
    point_list = []
    for score in my_list:
        point_list += score
        
    return(max(point_list))


# b
def find_max_score(my_list:list) -> float:
    scores = [sum(score) for score in my_list]
    return(max(scores))