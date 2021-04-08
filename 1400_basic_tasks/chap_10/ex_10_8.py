import numpy.random as npr
from collections import Counter

seq = npr.randint(2, 4, 15)

c = Counter(list(seq))
while c[2] != 7:
    seq = npr.randint(2, 4, 15)
    c = Counter(list(seq))
    
print('Ok, I\'m done!')