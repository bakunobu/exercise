import random

def random_walk(n: int) -> int:
    x, y = 0, 0
    i = 0
    while abs(x) < n and abs(y) < n:
        step = random.choice('s', 'w', 'e', 'n')
        if step == 's':
            y -= 1
        elif step == 'n':
            y += 1
        elif step == 'w':
            x -= 1
        else:
            x += 1
        i += 1
    return(i)


results = [random_walk(21) for x in range(100)]

print(sum(results)/len(results))