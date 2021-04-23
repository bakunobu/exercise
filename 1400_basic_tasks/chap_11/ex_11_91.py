def mean_weight(weghts:list) -> tuple:
    fat_people = [x for x in weights if x > 100]
    reg_people = [x for x in weights if x <= 100]
    fat_mean = sum(fat_people) / len(fat_people)
    reg_mean = sum(reg_people) / len(reg_people)
    return(fat_mean, reg_mean)