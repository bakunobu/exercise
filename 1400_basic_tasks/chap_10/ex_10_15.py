import numpy.random as npr
from collections import Counter


def dice() -> int:
    return(npr.randint(1,7))


def game_scores(n:int=100) -> None:
    res = [dice() for i in range(n)]
    c = Counter(res)
    for j in range(1, 7):
        print(f'{j}: {round(c[j]/n, 5)}')
        
        
game_scores(100)
game_scores(1000)