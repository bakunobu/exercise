def calc_cubes(n:int) -> int:
    nums = [1,]
    for x in range(2, n+1):
        # print(x, end='->')
        op = nums[-1]
        for i in range(x):
            op += 2
            nums.append(op)
            # print(op, end=', ') 
    total = sum(nums[-n:])
    return(total)

for x in range(1, 6):
    print(calc_cubes(x))