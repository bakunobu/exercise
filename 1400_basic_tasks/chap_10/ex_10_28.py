import numpy as np
import numpy.random as npr
import math

def eucl_dist(A:tuple, B:tuple=(0,0)) -> float:
    return(math.sqrt((A[0] - B[0])** 2 + (A[1] - B[1]) ** 2))


def sampling(n:int=100_000) -> float:
    samples = [(npr.uniform(-1,1),
                npr.uniform(-1,1)) for x in range(n)]
    ins = [1 for A in samples if eucl_dist(A) <= 1]
    return(len(ins)/n)


aver_pi = np.array([4 * sampling() for x in range(10)])

print(f'Calculated pi is {aver_pi.mean()}')
