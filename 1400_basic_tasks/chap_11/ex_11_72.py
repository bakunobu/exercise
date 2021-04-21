def sales_vol(sales:list, s:float) -> int:
    good_days = [1 for x in sales if x > s]
    return(len(good_days))