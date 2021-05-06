def two_fastest_cars(speed:list) -> tuple:
    max_price = 0
    t = 0
    for x in speed:
        if x > max_price:
            t = x - max_price
            max_price += t
        else:
            if max_price - x < t:
                t = max_price - x
    return(max_price,
           max_price - t)


