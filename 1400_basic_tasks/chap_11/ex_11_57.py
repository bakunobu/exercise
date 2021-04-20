# a
def more_moist(moist:list) -> int:
    if sum(moist[15:]) > sum(moist[:15]):
        return(2)
    else:
        return(1)
    
    
# b
def moist_decade(moist:list) -> int:
    dec_1 = sum(moist[:10])
    dec_2 = sum(moist[10:20])
    dec_3 = sum(moist[20:])
    dec_list ={dec_1:1,
               dec_2:2,
               dec_3:3}
    max_dec = max(dec_1, dec_2, dec_3)
    return(dec_list[max_dec])