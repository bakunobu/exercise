def calc_total(item_list:list, price_list:list) -> float:
    return(sum([a * b for a, b in zip(item_list,
                                      price_list)]))
    
    
print(calc_total([2, 3, 4], [1, 1, 1]))