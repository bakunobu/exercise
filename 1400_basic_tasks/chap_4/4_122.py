def which_region(x:float, y:float) -> str:
    if y < 2.5:
        return('III')
    elif y > 5.0:
        return('I')
    else:
        return('II')