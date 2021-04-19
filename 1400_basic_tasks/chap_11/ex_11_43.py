from typing import Union


def signum_list(a:list) -> Union[int, float]:
    pos_list = [x for x in a[::2]]
    neg_list = [-x for x in a[1::2]]
    return(sum(pos_list + neg_list))


