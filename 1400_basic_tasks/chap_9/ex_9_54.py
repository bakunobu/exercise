import math


for d in range(1,8):
    for n in range(1, d):
        if math.gcd(d,n) == 1:
            print(f'{n}/{d}')
        