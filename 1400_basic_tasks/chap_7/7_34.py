def class_heigth(n:int, i:int=2) -> list:
    heigth = []
    for j in range(i):
        h = 0
        for _ in range(n):
            while True:
                try:
                    x = float(input('Введит возраст ученика: '))
                    h += x
                    break
                except ValueError:
                    print('Используйте только числа (разделитель - \'.\')')
        heigth.append(h / n)
    return(heigth)