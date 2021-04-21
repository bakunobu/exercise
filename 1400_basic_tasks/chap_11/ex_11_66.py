def odd_even_moist(moist:list) -> bool:
    odd_days = moist[::2]
    even_days = moist[1::2]
    return(sum(even_days) > sum(odd_days))