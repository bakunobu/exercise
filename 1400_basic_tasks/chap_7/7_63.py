from main_funcs import get_input


def get_grades(n:int) -> tuple:
    grades = {2:0, 5:0}
    for x in range(n):
        g = get_input('Введите оценку: ', False)
        if g in grades.keys():
            grades[g]+=1
    return(grades[2], grades[5])

