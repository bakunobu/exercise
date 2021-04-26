def ge_mean_heigth(heigth:list) -> int:
    d = sum(heigth) / len(heigth)
    tall = [x for x in heigth if x > d]
    return(len(tall))