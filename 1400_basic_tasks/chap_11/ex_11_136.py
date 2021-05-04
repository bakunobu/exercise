def preferable_position(winds:list) -> int:
    wind_dict = {}
    for i in range(1, 9):
        wind_dict[winds.count(i)] = i
    
    min_result = min(list(wind_dict.keys))
    return(wind_dict.get(min_result, 0))