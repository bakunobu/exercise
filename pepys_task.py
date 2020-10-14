import random
import numpy as np

def play_series() -> tuple:
    i = []
    j = []

    for x in range(100):
        sixes = [random.randint(1, 6) for y in range(6)]
        i.append(sixes.count(1))
        twelwes = [random.randint(1, 6) for y in range(12)]
        if twelwes.count(1) > 1:
            j.append(twelwes.count(1))
        else:
            j.append(0)
        

    i = np.array(i)
    j = np.array(j)

    i_pos = np.where(i > 0)
    j_pos = np.where(j > 0)

    return(len(i_pos[0]),
           len(j_pos[0]))


def count_results(n: int) -> None:
    first = 0
    second = 0
    equal = 0
    for _ in range(n):
        f, s = play_series()
        if f > s:
            first += 1
        elif f < s:
            second += 1
        else:
            equal += 1
    
    print(f'Games played: {n}')
    print(f'1/6 leads {first},\n, 2/12 leads {second}\n(equal {equal})')
    

count_results(100)
    
