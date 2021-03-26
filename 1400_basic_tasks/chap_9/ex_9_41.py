def num_sum_eq(n:int=27) -> list:
    nums = []
    for a in range(1, 10):
        for b in range(1, 10):
            for c in range(1, 10):
                if a + b + c == n:
                    temp_nums = [a * 100 + b * 10 + c,
                                 a * 100 + c * 10 + b,
                                 b * 100 + a * 10 + c,
                                 b * 100 + c * 10 + a,
                                 c * 100 + a * 10 + b,
                                 c * 100 + b * 10 + a]
                    for x in temp_nums:
                        if x not in nums:
                            nums.append(x)
    return(sorted(nums))


# print(* num_sum_eq(11), sep='\n')