def less_m_mean(nums:list, m:float) -> float:
    le_m = [x for x in nums if x < m]
    return(sum(le_m) / len(le_m))