def show_nums(n:int) -> tuple:
    t = n // 10
    u = n % 10
    return(t, u)

def print_nums(n:int) -> None:
    for x in range(10, 100):
        nums = show_nums(x)
        if x % n == 0 or n in nums:
            print(x)
            
