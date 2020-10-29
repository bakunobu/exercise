"""
Составьте программу, выводящую инструкции по рисованию кривых дракона в по­рядке от О до 5. 
"""

"""
def draw_curve(n: int) -> str:
    
    # A simple helper for the dragon curve drawing
    
    # Args:
    # =====
    
    # Return:
    # =======
    # hint: str
    # an instruction
    

    curves = []
    turn_1 = 'L'
    turn_2 = 'R'
    for x in range(n):
        if x % 2 == 0:
            if curves:
                curve = curves[x - 1][1:] + 'L' + curves[x - 1][1:-1].replace(turn_1, turn_2) + 'F'
            else:
                curve = 'F'
        else:
            curve = curves[x - 1][1:] + 'L' + curves[x - 1][1:-1].replace(turn_2, turn_1) + 'F'
            
        curves.append(curve)
    return(''.join(curves))

for i in range(5):
    print(draw_curve(i))
"""

def inverse_replacer(my_str:str, a:str, b:str) -> str:
    """
    Replaces a wit b and b with a in my_str
    
    Args:
    =====
    my_str: str
    the sequence of symbols
    
    a: str
    if my_str[i] == a: my_str[i].replace(a, b)
    
    b: str
    if my_str[i] == b: my_str[i].replace(b, a)
    
    Return:
    =======
    new_str: str
    a result of replacement
    """
    
    my_str = list(my_str)
    print(my_str)
    for i in range(len(my_str)):
        if my_str[i] == a:
            my_str[i] = b
            continue
        elif my_str[i] == b:
            my_str[i] = a
            continue
    return(''.join(my_str[::-1]))


curves = []
for x in range(5):
    if x == 0:
        curve = 'F'
        curves.append(curve)
    elif x == 1:
        curve = curves[x-1] + 'L' + 'F'
        curves.append(curve)
    elif x == 2:
        curve = curves[x-1] + 'L' + inverse_replacer(curves[x-1], 'L', 'R')
        curves.append(curve)
    elif x == 3:
        curve = curves[x-1] + 'L' + inverse_replacer(curves[x-1], 'L', 'R')
        curves.append(curve)
    elif x == 4:
        curve = curves[x-1] + 'L' + inverse_replacer(curves[x-1], 'R', 'L')
        curves.append(curve)
    elif x == 5:
        curve = curves[x-1] + 'L' + inverse_replacer(curves[x-1], 'L', 'R')
        curves.append(curve)

for curve in curves:
    print(curves.index(curve), curve, sep=': ')
        

        