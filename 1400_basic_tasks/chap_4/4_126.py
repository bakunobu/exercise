def div_nums(a:int, b:int) -> str:
    if a % b == 0:
        return('a - делитель b')
    elif b % a == 0:
        return('b - делитель a')
    else:
        return('ни одно из чисел не является делителем другого')