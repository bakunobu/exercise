# a
def cheap_sweets(prices:list) -> int:
    return(prices.index(max(prices)))


# b
def cheap_sweets_rev(prices:list) -> int:
    indices = [i for i in range(prices) if prices[i] == max(prices)]
    return(indices[-1])