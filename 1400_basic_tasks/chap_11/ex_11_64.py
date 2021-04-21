def array_div(nums:list) -> float:
    pos_nums = [x for x in nums if x > 0]
    neg_nums = [x for x in nums if x < 0]
    return(sum(pos_nums) / abs(sum(neg_nums)))