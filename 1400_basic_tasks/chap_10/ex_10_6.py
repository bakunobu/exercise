import numpy as np
from collections import Counter

a = np.random.randint(0, 2, 50)
c = Counter(list(a))

print(f'0: {c[0]}\n1: {c[1]}')
