def find_nums(a: int) -> list:
    nums = []
    for _ in range(3):
        num = a % 10
        a //= 10
        nums.append(num)
    return(nums)


def count_nums(a:int=100, b:int=500) -> int:
    nums = [x for x in range(a, b+1) if sum(find_nums(x)) == 15]
    return(len(nums))

