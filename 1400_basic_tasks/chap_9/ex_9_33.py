def div_to_list(n:int) -> list:
    div_list = [x for x in range(1, n) if not n % x]
    return(div_list)


def find_friendster_nums(a:int=1, b:int=50_000) -> list:
    friend_nums = []
    for i in range(a, b+1):
        j = sum(div_to_list(i))
        if i != j and sum(div_to_list(j)) == i:
            if (j, i) not in friend_nums:
                friend_nums.append((i, j))
    return(friend_nums)
    
print(find_friendster_nums())