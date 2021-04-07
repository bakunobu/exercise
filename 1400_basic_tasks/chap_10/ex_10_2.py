import numpy as np


def int_input() -> int:
    while True:
        try:
            a = int(input('Введите целое число: '))
            return(a)
        except ValueError:
            print('Используйте только целые числа!')


# a
rand_nums = np.random.randint(0, 11, 10)

# print(* rand_nums)


# b
def return_k_nums():
    a = int_input()
    k = int_input()
    
    rand_nums = np.random.randint(0, a+1, k)
    return(rand_nums)

# print(* return_k_nums())


# c
rand_nums = np.random.randint(10, 21, 20)
# print(* rand_nums)


# d
def return_a_k_nums():
    a = int_input()
    k = int_input()
    
    rand_nums = np.random.randint(-10, a+1, k)
    return(rand_nums)


# print(* return_a_k_nums())


#e
def return_a_b_nums():
    k = np.random.randint(0, 15)
    a = int_input()
    b = int_input()
    
    rand_nums = np.random.randint(a, b+1, k)
    return(rand_nums)

print(return_a_b_nums())