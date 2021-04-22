def pos_neg_nums(nums:list) -> tuple:
    eps = nums.count(0)
    pos_neg = [1 if x > 0 else 0 for x in nums]
    return(pos_neg.count(1), pos_neg.count(0) - eps)
