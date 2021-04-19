def moist_per_dec(moist_list:list) -> tuple:
    dec_1 = sum(moist_list[:10])
    dec_2 = sum(moist_list[10:20])
    dec_3 = sum(moist_list[20:])
    return(dec_1, dec_2, dec_3)