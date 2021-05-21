def find_grade(grades:list, grade:int=2) -> int:
    return(grades.count(grade))


def is_grade_in_grades(grades:list, grade:int=2) -> bool:
    return(find_grade(grades, grade) > 0)


def print_is_grade(grades:list, grade:int=2) -> None:
    if is_grade_in_grades(grades, grade):
        print('Да!')
    else:
        print('Нет!')