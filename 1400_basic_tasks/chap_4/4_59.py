# a
def is_equalitarial(a:float, b:float,
                    c:float, eps:float=10e-8) -> bool:
        return(abs(a-b)<eps and abs(a-c)<eps and abs(b-c)<eps)

# b
def is_isiceles(a:float, b:float,
                c:float, eps:float=10e-8) -> bool:
    return(abs(a-b)<eps or abs(a-c)<eps or abs(b-c)<eps)