def is_prime(n:int) -> bool:
    divs = [1, ]
    nums = list(range(2, n+1))
    while nums:
        d = nums.pop(0)
        if not n % d:
            divs.append(d)
        nums = [x for x in range(d+1, n+1) if n % d != 0]
    return(len(divs) == 2 and divs[-1] == n)


def first_hund_primes() -> list:
    prime_list = []
    i = 2
    while len(prime_list) < 100:
        if is_prime(i):
            prime_list.append(i)
        i += 1
    return(prime_list)


print(first_hund_primes())