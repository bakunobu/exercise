def no_moist(moist:list) -> int:
    no_moist_days = ['*' for x in moist if x == 0]
    return(len(no_moist_days))