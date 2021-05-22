from typing import Union


def is_smaller(desc_list:list, a:Union[int, float]) -> Union[bool, int]:
    for i in range(len(desc_list)):
        if desc_list[i] < a:
            return(i)
    print('Элементов меньше {} в массиве нет!'.format(a))
    return(False)
