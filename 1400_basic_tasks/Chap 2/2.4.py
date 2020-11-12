def square_premeter(a: float) -> float:
    if a >= 0:
        return(a * 4)
    else:
        return(None)



for x in (1, 2, 3, 4, 0, -5):
    print(square_premeter(x))


