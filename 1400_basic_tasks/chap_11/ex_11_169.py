from typing import Union


# a
def add_heigth(studs:list, i:int, h:Union[int, float]) -> list:
    studs.insert(i, h)
    return(studs)


# b
def add_studs_bin(studs:list, h:Union[int, float]) -> list:
    for i in range(len(studs)):
        if h > studs[i]:
            studs.insert(i, h)
            return(studs)
    studs.append(h)
    return(studs)