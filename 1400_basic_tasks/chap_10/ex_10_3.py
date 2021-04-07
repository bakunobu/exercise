import numpy as np

def int_input() -> int:
    while True:
        try:
            a = int(input('Введите целое число: '))
            return(a)
        except ValueError:
            print('Используйте только целые числа!')


# получить и вывести на экран натуральные числа m и n, не превосходяще 20
n = np.random.randint(1, 20)
m = np.random.randint(1, 20)
print(f'n: {n}\nm: {m}')

# a, b
a = int_input()
b = int_input()
nat_nums = np.random.randint(a, b+1, n)
print(* nat_nums)


# floating point nums
fl_nums = np.random.uniform(0, n, (m,))
print(* fl_nums)