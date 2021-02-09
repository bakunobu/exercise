def print_prod() -> None:
    prod = 1
    while True:
        try:
            a = int(input('Введите число: '))
            prod *= a
            print(prod)
            if a == 0:
                break
        except ValueError:
            print('Используйте целые числа!')

