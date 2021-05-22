def is_greater(power:list, hp:int=200) -> bool:
    power.sort()
    return(power[-1] > 200)


powers = [100, 210, 190, 180, 90, 20, 25]

print(is_greater(powers))