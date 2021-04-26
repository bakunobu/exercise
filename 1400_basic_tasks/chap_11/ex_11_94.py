def boy_girl_heith(heith:list) -> bool:
    boys = [abs(x) for x in heigth if x < 0]
    girls = [x for x in heigth if x > 0]
    boys_mean = sum(boys) / len(boys)
    girls_mean = sum(girls) / len(girls)
    return(boys_mean - girls_mean > 10)