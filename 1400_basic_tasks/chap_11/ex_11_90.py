def pos_neg_mean(nums:list) -> tuple:
    pos_nums = [x for x in nums if x > 0]
    neg_nums = [x for x in nums if x < 0]
    pos_mean = sum(pos_nums) / len(pos_nums)
    neg_mean = sum(neg_nums) / len(neg_nums)
    return(pos_mean, neg_mean)