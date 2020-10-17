def is_prime(n: int) -> list:
    primes = []
    nums = [x for x in range(2, 10_000_000)]
    while nums:
        i = nums.pop(0)
        primes.append(i)
        nums = [x for x in nums if x % i != 0]
    return(primes)