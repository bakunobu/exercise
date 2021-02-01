# a
def rev_num(n:int) -> int:
    r_num  = 0
    while n:
        num = n % 10
        if r_num == 0:
            r_num = num
        else:
            r_num *= 10
            r_num += num
        n //= 10
    return(r_num)


# b
def add_two_two(n:int) -> int:
    i = 0
    num = n
    while n:
        n //= 10
        i += 1
    num += 2 * 10 ** i
    num *= 10
    num += 2
    return(num)


# c
def del_a(n:int, a:int) -> int:
    new_num = 0
    while n:
        num = n % 10
        if num == a:
            pass
        else:
            new_num *= 10
            new_num += num
        n //= 10
    return(new_num)


# d
def repl_firs_last(n:int) -> int:
    i = 0
    num = n
    while n:
        n //= 10
        i += 1
    first_dig = num // 10 ** (i - 1)
    last_dig = num % 10
    new_num = last_dig * 10 ** (i - 1)
    other_digs = num % 10 ** (i - 1)
    other_digs //= 10
    new_num += other_digs * 10
    new_num += first_dig
    return(new_num)


# e
def add_similar(n: int) -> int:
    i = 0
    num = n
    while n:
        n //= 10
        i += 1
    return(num + num * 10 ** i)

