import numpy.random as npr
import numpy as np


def generate_n_even(a:int, b:int, n:int) -> np.array:
    return(npr.randint(a, b+1, n))
