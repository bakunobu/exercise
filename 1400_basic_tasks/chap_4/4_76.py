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
    
# c
def king_move(a:int, b:int, c:int, d:int) -> bool:
    if abs(a - c) <= 1 and abs(b-d) <= 1:
        return(True)
    else:
        return(False)
    
# d
def queens_move(a:int, b:int, c:int, d:int) -> bool:
    if king_move(a,b,c,d) or rock_move(a,b,c,d):
        return(True)
    else:
        return(False)
    
# e
def first_move(a:int, b:int, c:int, d:int) -> bool:
    if a != 2:
        return(False)
    else:
        if b != d:
            return(False)
        elif 0 < c - a <= 2:
            return(True)
        else:
            return(False)

def regular_move(a:int, b:int, c:int, d:int) -> bool:
    if a >= c or b != d:
        return(False)
    elif c - a == 1:
        return(True)
    else:
        return(False)

def attack_move(a:int, b:int, c:int, d:int) -> bool:
    if abs(b - d) != 1:
        return(False)
    elif c-a != 1:
        return(False)
    else:
        return(True)

def white_pawn_move(a:int, b:int, c:int, d:int) -> bool:
        cond1 = first_move(a, b, c, d)
        cond2 = regular_move(a, b, c, d)
        cond3 = attack_move(a, b, c, d)
        return(cond1 or cond2 or cond3)
    
# f
def first_move(a:int, b:int, c:int, d:int) -> bool:
    if a != 7:
        return(False)
    else:
        if b != d:
            return(False)
        elif 0 < a - c <= 2:
            return(True)
        else:
            return(False)

def regular_move(a:int, b:int, c:int, d:int) -> bool:
    if a >= c or b != d:
        return(False)
    elif a - c == 1:
        return(True)
    else:
        return(False)

def attack_move(a:int, b:int, c:int, d:int) -> bool:
    if abs(b - d) != 1:
        return(False)
    elif a-c != 1:
        return(False)
    else:
        return(True)

def black_pawn_move(a:int, b:int, c:int, d:int) -> bool:
        cond1 = first_move(a, b, c, d)
        cond2 = regular_move(a, b, c, d)
        cond3 = attack_move(a, b, c, d)
        return(cond1 or cond2 or cond3)
    
# g
def knight_move(a:int, b:int, c:int, d:int) -> bool:
    if abs(a-c) == 1 and abs(b-d) == 2:
        return(True)
    elif abs(a-c) == 2 and abs(b-d) == 1:
        return(True)
    else:
        return(False)