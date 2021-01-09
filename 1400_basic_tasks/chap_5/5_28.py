def calc_prod(a, b) -> int:
    total = 1
    for x in range(a, b+1):
        total *= x
    return(total)


def int_input(question:str) -> int:
    while True:
        try:
            a = int(input(question))
            return(a)
        except ValueError:
            print('Используйте только целые числа!')
            

# a
print(calc_prod(7, 14))


# b
a = int_input('Введите число: ')
print(calc_prod(a, 15))


# c
b = int_input('Введите число: ')
print(calc_prod(1, b))


# d
a = int_input('Введите число: ')
b = int_input('Введите число: ')
print(calc_prod(a, b))

