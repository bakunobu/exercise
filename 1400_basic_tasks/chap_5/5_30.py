def int_input(question:str) -> int:
    while True:
        try:
            a = int(input(question))
            return(a)
        except ValueError:
            print('Используйте только целые числа!')


def calc_square(a:int, b:int) -> int:
    total = 0
    for x in range(a, b+1):
        total += x ** 2
    return(total)
    
            
# a
def calc_cubes(a:int, b:int) -> int:
    total = 0
    for x in range(a, b+1):
        total += x ** 3
    return(total)


print(calc_cubes(25, 40))


# b
a = int_input('Введите число: ')
print(calc_square(a, 50))


# c
n = int_input('Введите число: ')
print(calc_square(1, n))


# d
a = int_input('Введите число: ')
b = int_input('Введите число: ')
print(calc_square(a, b))