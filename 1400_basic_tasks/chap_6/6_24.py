# a
def show_sum(n:int) -> int:
    nums = []
    while n:
        num = n % 10
        nums.append(num)
        n //= 10
    num_sum = 0
    i = 1
    while nums:
        a = nums.pop()
        num_sum += (a * 1)
        i *= -1
    return(num_sum)

    
# b
def show_sum(n:int) -> int:
    nums = []
    while n:
        num = n % 10
        nums.append(num)
        n //= 10
    num_sum = 0
    i = 1
    while nums:
        a = nums.pop(0)
        num_sum += (a * 1)
        i *= -1
    return(num_sum)
    