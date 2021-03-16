def collect_grades() -> list:
    journal = [[] for i in range(18)]
    for i in range(18):
        msg = f'Введите оценки {i+1} ученика: '
        while True:
            try:
                a, b, c = [int(x) for x in input(msg).split()]
                break
            except ValueError:
                print('Используйте целые числа')
        journal[i] = [a, b, c,]
    return(journal)


# a
def calc_a_grades(my_list:list) -> int:
    a_grades = [1 for record in my_list for i in record if i == 5]
    return(len(a_grades))

# grades = collect_grades()

# print(calc_a_grades(grades))


# b
def calc_c_grades(my_list:list) -> list:
    c_grades = [record.count(3) for record in my_list]
    return(c_grades)


# c
def calc_d_grades(my_list) -> list:
    subj_one = [1 for record in my_list if record[0] == 2]
    subj_two = [1 for record in my_list if record[1] == 2]
    subj_three = [1 for record in my_list if record[2] == 2]
    return([subj_one, subj_two, subj_three,])