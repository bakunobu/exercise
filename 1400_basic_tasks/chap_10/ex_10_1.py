import numpy as np
import math

# a
def generate_rand_seq(n:int=8) -> np.array:
    return(np.random.random(size=n))


# print(* generate_rand_seq())

# b
def generate_rand_seq(k:int) -> np.array:
    return(np.random.random(size=k))

# c 
# print(* generate_rand_seq(15))

# d
# print(* generate_rand_seq(20))
 
# e
def float_gen():
    msg = 'Укажите значения a и b (через пробел): '
    while True:
        try:
            a, b = [float(x) for x in input(msg).split()]
            if a > 0 and b > 0:
                break
        except ValueError:
            print('Используйте пробел для \
    разделения чисел и . для отделения дробной части')
            
    k = np.random.randint(1, math.ceil(a))

    seq = np.random.uniform(0, math.ceil(b), (k,))

    return(seq)

# f
seq = np.random.uniform(-40, 40, (10,))
print(* seq)


# g
def adv_float_gen():
    while True:
        try:
            m = int(input('Введите число m: '))
            if m > 0:
                break
        except ValueError:
            print('Используйте целые числа больше 0')
    
    msg = 'Укажите значения a и b (через пробел): '
    while True:
        try:
            a, b = [float(x) for x in input(msg).split()]
            if a > 0 and b > 0:
                break
        except ValueError:
            print('Используйте пробел для \
    разделения чисел и . для отделения дробной части')
            
    k = np.random.randint(1, m)

    seq = np.random.uniform(math.ceil(a), math.ceil(b), (k,))

    return(seq)

print(* adv_float_gen())