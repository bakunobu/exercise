def mut_prime(m:int, n:int) -> None:
    i = min(m, n)
    while i < m * n:
        i += 1
        if i % m == 0 or i % n == 0:
            print(i)