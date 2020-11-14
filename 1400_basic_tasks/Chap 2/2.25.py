def area_and_volume(a:float, b:float, h:float) -> float:
    area = 2 * a * b + 2 * a * h + 2 * b * h
    vol =  a * b * h
    return(area, vol)

print(area_and_volume(3, 4, 2))
    