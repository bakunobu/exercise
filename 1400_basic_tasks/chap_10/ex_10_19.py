import random


def show_rank() -> None:
    ranks = ['6', '7', '8', '9', '10',
             'J', 'Q', 'K', 'A']
    
    r = random.sample(ranks, 1)
    print(f'{r[0]}')
    
    
show_rank()