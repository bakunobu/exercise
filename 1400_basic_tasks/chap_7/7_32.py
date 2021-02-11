def class_age(i:int=2, n:int=20) -> list:
    ages = []
    for j in range(i):
        age = 0
        for _ in range(n):
            while True:
                try:
                    x = float(input('Введит возраст ученика: '))
                    age += x
                    break
                except ValueError:
                    print('Используйте только числа (разделитель - \'.\')')
        ages.append(age / n)
    return(ages)