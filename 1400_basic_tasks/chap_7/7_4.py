def wight_summator(n:int) -> float:
    weight = 0


    for x in range(n):
        while True:
            try:
                a = float(input('Введите число: '))
                weight += a
                break
            except ValueError:
                print('Вы ввели не число!')
        
    return(weight)