import numpy.random as npr


def domino() -> tuple:
    return(npr.randint(0,7), npr.randint(0,7))


def print_domino(values:tuple) -> None:
    print(f'''* * *
* {values[0]} *
* * *
* {values[1]} *
* * *''')
    
def dull_domino(values:tuple) -> None:
    print(f'Выбрана кость {values[0]}-{values[1]}')
    
    
a = domino()
dull_domino(a)
print_domino(a)

