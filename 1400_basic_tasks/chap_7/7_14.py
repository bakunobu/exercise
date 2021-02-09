def give_num() -> float:
    while True:
        try:
            a = float(input('Введите число: '))
            return(a)
        except ValueError:
            print('Используйте только числа (разделитель - \'.\')')



def sum_n_squares(n:int) -> float:
    numbers = [give_num() ** 2 for x in range(n)]
    return(sum(numbers))


print(sum_n_squares(10))