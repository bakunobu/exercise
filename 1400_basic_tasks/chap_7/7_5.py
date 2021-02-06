def salary_summator(n:int) -> float:
    salary = 0


    for x in range(n):
        while True:
            try:
                a = float(input('Введите число: '))
                salary += a
                break
            except ValueError:
                print('Вы ввели не число!')
        
    return(salary)