def count_cubes(n:int) -> int:
    total = n ** 2
    for x in range(1, n+1):
        total += (x + n) ** 2
    return(total)