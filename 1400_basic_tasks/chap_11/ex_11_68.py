def not_neg_nums(nums:list) -> int:
    not_neg = [x for x in nums if x >= 0]
    return(len(not_neg))