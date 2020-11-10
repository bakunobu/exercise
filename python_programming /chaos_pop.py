

def count_pop_dynamix(r: float, x: float) -> float:
    return(r * x * (1 - x))


def set_experiment(r: float, x:float=0.01, n: int=100) -> None:
    for _ in range(1, n+1):
        x = count_pop_dynamix(r, x)
        if x > 1.0:
            x = 1
        print(f'Step: {_}, population: {x}')
        
"""       
for r in (3.5, 3.8, 5.0):
    print(f'Coef: {r}')
    set_experiment(r)
"""

for r in range(5, 35, 10):
    r /= 10
    print(1 - 1 / r)
    set_experiment(r)