def par_res(n:int) -> float:
    res = 0
    for x in range(n):
        while True:
            try:
                r = float(input('Введите число: '))
                res += 1 / r
                break
            except ValueError:
                print('Используйте только числа (разделитель \'.\')')
    return(res)
    