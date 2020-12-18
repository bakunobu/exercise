# a
def rock_move(a:int, b:int, c:int, d:int) -> bool:
    if a == c or b == d:
        return(True)
    else:
        return(False)
    

# b
def bishop_move(a:int, b:int, c:int, d:int) -> bool:
    if abs(a - c) == abs(b - d):
        return(True)
    else:
        return(False)