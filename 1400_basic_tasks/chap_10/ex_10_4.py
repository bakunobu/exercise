import numpy as np


a = np.random.randint(0, 4, 50)
b = [x for x in list(a) if x in (0, 1)]


print(len(b))
print(* b)