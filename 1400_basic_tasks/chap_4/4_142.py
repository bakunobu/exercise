months_dict ={1: 'Jan',
               2: 'Feb',
               3: 'Mar',
               4: 'Apr',
               5: 'May',
               6: 'Jun',
               7: 'Jul',
               8: 'Aug',
               9: 'Sep',
               10: 'Oct',
               11: 'Now',
               12: 'Dec'}


def which_month(n: int) -> str:
    i = n % 12
    return(months_dict.get(i))