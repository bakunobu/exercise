def bigger_prod(n:int, s:float) -> bool:
    my_prod = 1
    for i in range(n):
        while True:
            try:
                x = float(input('Введите число: '))
                my_prod *= x
                break
            except ValueError:
                print('Используйте только числа (разделитель - \'.\')')
    return(my_prod > s)
        