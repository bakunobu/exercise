# a

def two_max_num(n:int, from_left:bool=True) -> tuple:
    length = 0 
    max_one = 0
    pos_one = None
    max_two = 1
    pos_two = None
    while n:
        num = n % 10
        if num > max_two:
            max_one, max_two = max_two, num
            pos_one, pos_two = pos_two, length
        elif num > max_one:
            max_one = num
            pos_one = length
        n //= 10
        length += 1
    if from_left:
        return(pos_one, pos_two)
    else:
        return(length - pos_one - 1,
               length - pos_two - 1)
        

# b
def two_max_num(n:int, from_left:bool=True) -> tuple:
    length = 0 
    min_one = 9
    pos_one = None
    min_two = 8
    pos_two = None
    while n:
        num = n % 10
        if num < min_two:
            min_one, min_two = min_two, num
            pos_one, pos_two = pos_two, length
        elif num < min_one:
            min_one = num
            pos_one = length
        n //= 10
        length += 1
    if from_left:
        return(pos_one, pos_two)
    else:
        return(length - pos_one - 1,
               length - pos_two - 1)
        