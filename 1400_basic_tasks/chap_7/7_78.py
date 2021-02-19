from main_funcs import get_input


def phys_grades(n:int) -> tuple:
    grades_dict = {5:0,
                   4:0,
                   3:0,
                   2:0}
    
    for x in range(n):
        grade = get_input('Укажите оценку: ', False)
        grades_dict[grade] += 1
    
    return(grades_dict[5],
           grades_dict[4],
           grades_dict[3],
           grades_dict[2])