# a
def count_a(n:int) -> int:
    while True:
        try:
            a = int(input('Введите число: '))
            if 0 <= a <= 8:
                break
        except ValueError:
            print('Только числа')
    counter = 0
    while n:
        num = n % 10
        if num == a:
            counter += 1
        n //= 10
    return(counter)


# b
def count_a(n:int) -> int:
    while True:
        try:
            a = int(input('Введите число: '))
            if 0 <= a <= 8:
                break
        except ValueError:
            print('Только числа')
    total = 0
    while n:
        num = n % 10
        if num > a:
            total += num
        n //= 10
    return(total)


# c
def count_a(n:int) -> int:
    total = 0
    while n:
        num = n % 10
        if num % 2 == 0:
            total += num
        n //= 10
    return(total)


# d
def count_a(n:int, x:int, y:int) -> int:
    counter = 0
    while n:
        num = n % 10
        if num in (x, y):
            counter += 1
        n //= 10
    return(counter)