def print_squares() -> None:
    while True:
        try:
            n = int(input('Введите число: '))
            break
        except ValueError:
            print('Используйте целые числа!')
    i = 1
    while i ** 2 <= n:
        
        i += 1
    
    print(i ** 2)
        
print_squares()