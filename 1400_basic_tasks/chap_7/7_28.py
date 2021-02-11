def mean(n:int=10) -> float:
    my_sum = 0
    for i in range(n):
        while True:
            try:
                x = int(input('Введите число: '))
                my_sum += x
                break
            except ValueError:
                print('Используйте только целые числа')
    return(my_sum / n)