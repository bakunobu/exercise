def ge_mean_heigth(height:list) -> int:
    d = sum(height) / len(height)
    tall = [x for x in heigth if x > d]
    return(len(tall))