def calc_mean_moist(moist:list) -> float:
    return(sum(moist) / len(moist))


def calc_variance(moist:list) -> list:
    m = calc_mean_moist(moist)
    var_moist = [x - m for x in moist]
    return(var_moist)

