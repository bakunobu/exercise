def find_nums(a: int) -> list:
    nums = []
    for _ in range(3):
        num = a % 10
        a //= 10
        nums.append(num)
    return(sum(nums))


def count_num(a:int=100, b:int=1000) -> int:
    nums = []
    for x in range(a, b):
        if x % 7 == 0 and find_nums(x) % 7 == 0:
            nums.append(x)
    return(len(nums))


print(count_num())