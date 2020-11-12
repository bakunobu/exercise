

def calc_area(a: float) -> float:
    A = 6 * a ** 2
    return(A)

def calc_vol(a: float) -> float:
    V = a ** 3
    return(V)

def show_res(a: float) -> None:
    print('Area of the square\'s sides: %0.2f'
          % calc_area(a))
    print('Volume of the square %0.2f' %
          calc_vol(a))
    
show_res(4)