import numpy.random as npr
from collections import Counter

freq_100 = npr.randint(0, 2, 100)
freq_1000 = npr.randint(0, 2, 1000)
c_100 = Counter(list(freq_100))
c_1000 = Counter(list(freq_1000))


print("100:")
print(f'0: {c_100[0] / 100}, 1: {1- c_100[0] / 100}')
print('1000:')
print(f'0: {c_1000[0] / 1000}, 1: {1- c_1000[0] / 1000}')