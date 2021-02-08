def seq_sum() -> int:
    my_sum = 0
    while True:
        try:
            a = int(input('Введите число: '))
            if a == 0:
                break
            my_sum += a
        except ValueError:
            print('Используйте целые числа')
    return(my_sum)