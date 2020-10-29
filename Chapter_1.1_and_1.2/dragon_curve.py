"""
Составьте программу, выводящую инструкции по рисованию кривых дракона в по­рядке от О до 5. 
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

    for i in range(len(my_str)):
        
        if my_str[i] == a:
            my_str[i] = b
            continue
        
        elif my_str[i] == b:
            my_str[i] = a
            continue
        
    return(''.join(my_str[::-1]))



def draw_curve(n: int) -> str:
    
    # A simple helper for the dragon curve drawing
    
    # Args:
    # =====
    
    # Return:
    # =======
    # hint: str
    # an instruction
    

    curves = []

    for x in range(n):
        if x == 0:
            curve = 'F'
            curves.append(curve)
        elif x == 1:
            curve = curves[x-1] + 'L' + 'F'
            curves.append(curve)
        elif x == 2:
            curve = curves[x-1] + 'L' + inverse_replacer(curves[x-1], 'L', 'R')
            curves.append(curve)
        else:
            
            if x % 2 == 0:
                curve = curves[x-1] + 'L' + inverse_replacer(curves[x-1], 'R', 'L')
                curves.append(curve)
            
            else:
                curve = curves[x-1] + 'L' + inverse_replacer(curves[x-1], 'L', 'R')
                curves.append(curve)
    
    return(curves)

curves = draw_curve(5)

for curve in curves:
    print(curves.index(curve), curve, sep=': ')
        

        