def calc_mean(a:int, b:int) -> float:
    delim = b - a + 1
    total = 0
    for x in range(a, b + 1):
        total += x
        
    return(total / delim)


def int_input(question:str) -> int:
    while True:
        try:
            a = int(input(question))
            return(a)
        except ValueError:
            print('Используйте только целые числа!')

# a
print(calc_mean(1, 750))


# b
b = int_input('Введите число: ')
print(calc_mean(150, b))


# c
a = int_input('Введите число: ')
print(calc_mean(a, 200))


# d
a = int_input('Введите число: ')
b = int_input('Введите число: ')
print(calc_mean(a, b))