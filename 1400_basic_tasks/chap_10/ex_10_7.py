import numpy as np

# a
a = np.random.randint(0,3)
b = np.random.randint(0,4)

while a == b:
    a = np.random.randint(0,3)
    b = np.random.randint(0,4)
    
print(f'a: {a}, b: {b}')


# b
a = np.random.randint(1,3)
b = np.random.randint(0,3)
c = np.random.randint(1,4)

while len(set((a, b, c))) != 3:
    a = np.random.randint(1,3)
    b = np.random.randint(0,3)
    c = np.random.randint(1,4)
    
print(f'a: {a}, b: {b}, c: {c}')
