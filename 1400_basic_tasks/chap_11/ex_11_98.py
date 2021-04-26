def le_mean_price(price:list) -> int:
    d = sum(price) / len(price)
    cheap = [x for x in price if x < d]
    return(len(cheap))