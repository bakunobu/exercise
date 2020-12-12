def same_height(a:float, b:float, c:float,
                eps:float=10e-8) -> bool:
    return(abs(a-b)<eps and abs(a-c)<eps and abs(b-c)<eps)