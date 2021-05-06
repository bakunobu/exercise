def max_second_max(nums:list) -> tuple:
    max_el = None
    second_el = None
    for num in nums:
        if max_el is None:
            max_el = num
        elif second_el is None:
            max_el, second_el = max(num, max_el), min(num, max_el)
        elif num > second_el:
            max_el, second_el = max(num, max_el), min(num, max_el)
        else:
            continue
    
    return(max_el,
           second_el)
    
    
def max_prices(price:list) -> tuple:
    return(max_second_max(price))

