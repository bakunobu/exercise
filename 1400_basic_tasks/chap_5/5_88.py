def find_nums(a: int) -> list:
    nums = []
    for _ in range(3):
        num = a % 10
        a //= 10
        nums.append(num)
    return(nums)


def count_nums(a:int=100, b:int=501) -> int:
    nums = [x for x in range(a, b) if 0 < sum(find_nums(x)) <= 27]
    return(len(nums))
