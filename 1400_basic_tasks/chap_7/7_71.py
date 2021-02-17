from main_funcs import get_input


def subj_grades(n:int) -> int:
    grade_2 = 0
    msg = 'Введите оценки по двум предметам (через пробел): '
    for _ in range(n):
        while True:
            try:
                subj_one, subj_two = [int(x) for x in input(msg).split(' ')]
                if subj_one == 2:
                    grade_2 += 1
                if subj_two == 2:
                    grade_2 +=1
                break
            except ValueError:
                print('Используйте целые числа!')
    return(grade_2)

print(subj_grades(5))