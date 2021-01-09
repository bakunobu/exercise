def calc_sum(a:int, b:int) -> int:
    total = 0
    for x in range(a, b+1):
        total += x
        
    return(total)


def int_input(question:str) -> int:
    while True:
        try:
            a = int(input(question))
            return(a)
        except ValueError:
            print('Используйте только целые числа!')


# a
print(calc_sum(200, 600))


# b
def calc_sum_b() -> int:
    a = int_input('Введите число: ')
    return(calc_sum(a, 400))


# c
def calc_sum_c() -> int:
    b = int_input('Введите число: ')
    return(calc_sum(-15, b))


# d
def calc_sum_d() -> int:
    a = int_input('Введите число: ')
    b = int_input('Введите число: ')
    return(calc_sum(a, b))

