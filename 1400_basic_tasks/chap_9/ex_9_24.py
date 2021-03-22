def num_div(n:int) -> int:
    n_divs = 0
    for x in range(1, n+1):
        if not n % x:
            n_divs += 1
    return(n_divs)


def count_divs(a, b) -> dict:
    div_counter = {}
    for i in range(a, b+1):
        n_divs = num_div(i)
        div_counter[i] = n_divs
    return(div_counter)


# a
def find_max_num_div(div_counter:dict) -> int:
    nums = []
    num_divs = []
    for k, v in sorted(div_counter.items()):
        nums.append(k)
        num_divs.append(v)
    max_div = max(num_divs)
        
    max_divs = [key for key in div_counter.keys() if div_counter[key] == max_div]
    return(max(max_divs))


# my_dict = count_divs(1, 9)
# print(find_max_num_div(my_dict))


# b
def find_min_num_div(div_counter:dict) -> int:
    nums = []
    num_divs = []
    for k, v in sorted(div_counter.items()):
        nums.append(k)
        num_divs.append(v)
    max_div = max(num_divs)
        
    max_divs = [key for key in div_counter.keys() if div_counter[key] == max_div]
    return(min(max_divs))


# my_dict = count_divs(1, 9)
# print(find_min_num_div(my_dict))