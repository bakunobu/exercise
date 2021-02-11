def aver_moist(i:int=2, n:int=31) -> list:
    moist = []
    for j in range(i):
        falls = 0
        for _ in range(n):
            while True:
                try:
                    x = float(input('Введит возраст ученика: '))
                    falls += x
                    break
                except ValueError:
                    print('Используйте только числа (разделитель - \'.\')')
        moist.append(falls / n)
    return(moist)