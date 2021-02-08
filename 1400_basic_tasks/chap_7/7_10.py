
def calc_grades(n:int, i:int) -> list:
    grades = []
    for x in range(n):
        total = 0
        for j in range(i):
            try:
                grade = int(input('Введите оценку'))
                total += grade
            except ValueError:
                print('Используйте числа')
        grades.append(total)
    return(grades)


print(* calc_grades(2, 5))