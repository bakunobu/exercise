def mean_moist(moist:list) -> float:
    rainy = [x for x in moist if x > 0]
    return(sum(rainy) / len(rainy))