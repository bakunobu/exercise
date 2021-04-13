import math
import matplotlib.pyplot as plt
import numpy as np


def func(x:float) -> float:
    return(math.sin(x))


X = np.linspace(0, 3.15, 300)
Y = [func(x) for x in X]


# plt.plot(X, Y)
# plt.show()

ins = 0
n = 1000

for x in range(n):
    x = np.random.uniform(0, 3.151)
    y = np.random.uniform(0, max(Y))
    if y <= func(x):
        ins += 1
print(3.15 * (ins / n))

    