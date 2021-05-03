# a
def oldest_pers(ages:list) -> int:
    oldest = ages[0]
    oldest_ind = 0
    for i in range(1, len(ages)):
        if ages[i] > oldest:
            oldest = ages[i]
            oldest_ind = i
    return(i)


# b
def rev_oldest_pers(ages:list) -> int:
    oldest = None
    oldest_ind = None
    for i in range(len(ages)):
        if oldest is None:
            oldest = ages[i]
            oldest_ind = i
        if ages[i] >= oldest:
            oldest = ages[i]
            oldest_ind = i
    
    return(oldest_ind)
            