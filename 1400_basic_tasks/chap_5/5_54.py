def calc_els(a:float, n:int) -> list:
    nums = []
    for i in range(1, n + 1):
        num = 1
        for j in range(i):
            num *= a
        nums.append(num)
    return(nums)