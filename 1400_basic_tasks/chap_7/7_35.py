def class_grades(n:int, i:int=2) -> list:
    grades = []
    for j in range(i):
        grade = 0
        for _ in range(n):
            while True:
                try:
                    x = int(input('Введит возраст ученика: '))
                    grade += x
                    break
                except ValueError:
                    print('Используйте только целые числа')
        grades.append(grade / n)
    return(grades)