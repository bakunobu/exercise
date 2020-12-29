def which_region(x:float, y:float) -> str:
    if x < 1:
        return('I')
    elif x > 5:
        return('III')
    else:
        return('II')