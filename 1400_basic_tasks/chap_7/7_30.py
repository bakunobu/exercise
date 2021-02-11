def mean(n:int ) -> float:
    my_sum = 0
    for i in range(n):
        while True:
            try:
                x = float(input('Введите число: '))
                my_sum += x
                break
            except ValueError:
                print('Используйте только числа (разделитель - \'.\')')
    return(my_sum / n)