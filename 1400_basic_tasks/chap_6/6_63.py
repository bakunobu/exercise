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


def is_palindrome_num(n:int) -> bool:
    r_num = rev_num(n)
    return(n == r_num)
