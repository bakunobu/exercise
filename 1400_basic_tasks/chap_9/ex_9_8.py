def collect_grades() -> list:
    journal = [[] for i in range(14)]
    for i in range(14):
        msg = f'Введите оценки {i+1} студента: '
        while True:
            try:
                a, b, c = [int(x) for x in input(msg).split()]
                break
            except ValueError:
                print('Используйте целые числа')
        journal[i] = [a, b, c,]
    return(journal)


# a
def calc_good_studs(my_list:list) -> int:
    good_studs = [1 for i in my_list if 2 not in i]
    return(len(good_studs))

# b
def calc_good_grades_per_subj(my_list:list) -> tuple:
    subj_one = [1 for i in my_list if i[0] == 4 or i[0] == 5]
    subj_two = [1 for i in my_list if i[1] == 4 or i[1] == 5]
    subj_three = [1 for i in my_list if i[2] == 4 or i[2] == 5]
    good_subj = []
    for i in range(3):
        if len([subj_one, subj_two, subj_three][i]) == 14:
            good_subj.append(f'Subject {i+1}')
    return(good_subj)


grades = collect_grades()
print(calc_good_grades_per_subj(grades))


# c
def calc_d_grades_per_subj(my_list:list) -> tuple:
    subj_one = [1 for i in my_list if i[0] == 2]
    subj_two = [1 for i in my_list if i[1] == 2]
    subj_three = [1 for i in my_list if i[2] == 2]
    return(len(subj_one),
           len(subj_two),
           len(subj_three))

