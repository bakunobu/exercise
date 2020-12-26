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



fig_funcs = {'ладья': rock_move(),
             'ферзь': queens_move(),
             'конь': knight_move(),
             'слон': bishop_move(),
             'король': king_move()}


def turn_func(fig_1:str, fig_2:str,
              a:int=2, b:int=2,
              c:int=3, d:int=3,
              e:int=4, f:int=4) -> bool:
    func_1 = fig_funcs.get(fig_1)
    func_2 = fig_funcs.get(fig_2)
    if func_1(a, b, e, f):
        if func_2(c, d, e, f):
            return(False)
        else:
            return(True)
    else:
        return(False)

# a
turn_func('ладья', 'ладья')


# b
turn_func('ладья', 'ферзь')


# c
turn_func('ладья', 'конь')


# d
turn_func('ладья', 'слон')


#e
turn_func('ферзь', 'ферзь')


# f
turn_func('ферзь', 'ладья')


# g
turn_func('ферзь', 'конь')


# h
turn_func('ферзь', 'слон')


# j
turn_func('конь', 'конь')


# k
turn_func('конь', 'ладья')


# l
turn_func('конь', 'ферзь')


# m
turn_func('конь', 'слон')


# n
turn_func('слон', 'слон')


# o
turn_func('слон', 'ферзь')


# p
turn_func('слон', 'конь')


# q
turn_func('слон', 'ладья')


# r
turn_func('король', 'слон')


# s
turn_func('король', 'ферзь')


# t
turn_func('король', 'конь')


# u
turn_func('король', 'ладья')