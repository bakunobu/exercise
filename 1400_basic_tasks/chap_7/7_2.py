def n_plus_ten_els(n:float) -> float:
    my_sum = 0
    my_sum += n

    for x in range(10):
        while True:
            try:
                a = float(input('Введите число: '))
                my_sum += a
                break
            except ValueError:
                print('Вы ввели не число!')
    
    return(my_sum)