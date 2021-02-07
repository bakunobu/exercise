def res_summator(n:int) -> float:
    resist = 0


    for x in range(n):
        while True:
            try:
                a = float(input('Введите число: '))
                resist += a
                break
            except ValueError:
                print('Вы ввели не число!')
        
    return(resist)