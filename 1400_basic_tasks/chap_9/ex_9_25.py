def is_prime(n:int) -> bool:
    divs = [1, ]
    nums = list(range(2, n+1))
    while nums:
        d = nums.pop(0)
        if not n % d:
            divs.append(d)
        nums = [x for x in range(d+1, n+1) if n % d != 0]
    return(len(divs) == 2 and divs[-1] == n)


def all_primes(start=101, end=1000) -> list:
    prime_nums = []
    for i in range(start, end, 2):
        if is_prime(i):
            prime_nums.append(i)
    return(prime_nums)


print(all_primes()[:10])


        