import numpy.random as npr
import random

def create_dominos() -> list:
    dominos = [(a, b) for a in range(1, 7) for b in range(1, 7)]
    return(dominos)


def dull_domino(values:tuple) -> None:
    print(f'Выбрана кость {values[0]}-{values[1]}')


def combine() -> bool:
    dominos = create_dominos()
    dom_a, dom_b = random.sample(dominos, 2)
    dull_domino(dom_a)
    dull_domino(dom_b)
    return(len(set(dom_a).intersection(set(dom_b))) > 0)


for i in range(25):
    print(combine())
    