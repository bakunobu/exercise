def no_miost(moist:list) -> bool:
    dry = [x for x in moist if x == 0]
    return(len(dry) == 10)