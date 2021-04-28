def max_hot_week(temper:list) -> list:
    hot_days = temper[:7]
    max_sum = sum(temper[:7])
    for i in range(1, len(temper) - 7):
        if sum(temper[i:i+7]) > max_sum:
            max_sum = sum(temper[i:i+7])
            hot_days = temper[i:i+7]
    return(hot_days)