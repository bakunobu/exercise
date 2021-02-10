def is_bigger_ten_k(n:int=8, lim:int=10_000) -> bool:
    prod = 1
    for x in range(n):
        while True:
            try:
                i = float(input('Введите число: '))
                prod *= i
                break
            except ValueError:
                print('Используйте только числа (разделитель - \'.\')')
    return(prod < lim)