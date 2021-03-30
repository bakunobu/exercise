def dig_sum(x:int) -> int:
    digs = []
    while x:
        a = x % 10
        x //= 10
        digs.append(a)
    return(sum(digs))
        

def square_m_n(m:int, n:int) -> list:
    nums = []
    for x in range(n):
        num = dig_sum(x)
        if num ** 2 == m:
            nums.append(num)
    return(nums)


