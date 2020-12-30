def find_quarter(x:float, y:float) -> str:
    if x > 0 and y > 0:
        return('I')
    elif x > 0 and y < 0:
        return('IV')
    elif x < 0 and y > 0:
        return('II')
    else:
        return('III')