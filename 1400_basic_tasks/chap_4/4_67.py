def num_to_dig(a:int) -> list:
    h = a // 100
    h -= a * 100
    t = a // 10
    u = a % 10
    return(h, t, u)


def is_lucky(a:int) -> bool:
    num_1 = a // 1000
    num_2 = a % 1000
    sum_1 = sum(num_to_dig(num_1))
    sum_2 = sum(num_to_dig(num_2))
    return(sum_1 == sum_2)