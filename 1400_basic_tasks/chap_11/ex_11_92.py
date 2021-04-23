def boys_girls_maen(heigth:list) -> tuple:
    girls = [x for x in heigth if x > 0]
    boys = [abs(x) for x in heigth ud x < 0]
    girls_mean = sum(girls) / len(girls)
    boys_mean = sum(boys) / len(boys)
    return(boys_mean, girls_mean)