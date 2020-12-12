def two_of_three(a:float, b:float, c:float,
                 eps:float=10e-8) -> bool:
    return(abs(a-b)<eps or abs(a-c)<eps or abs(b-c)<eps)


