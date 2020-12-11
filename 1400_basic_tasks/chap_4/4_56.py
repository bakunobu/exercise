def is_symmetrical(x:int) -> bool:
    th = x // 1000
    x -= th * 1000
    hund = x // 100
    x -= hund * 100
    tens = x // 10
    units = x % 10
    num_1 = th + hund * 10
    num_2 = tens * 10 + units
    return(num_1 == num_2)


print(is_symmetrical(1441))