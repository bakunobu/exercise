def greater_ten_mean(nums:list) -> float:
    gt_ten = [x for x in nums if x > 10]
    return(sum(gt_ten) / len(gt_ten))