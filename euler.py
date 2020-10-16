from datetime import datetime
start = datetime.now()

pos_e = [e ** 5 for e in range(150, 1, -1)]




def find_diffs(my_list):
    diffs = [b for a in my_list for b in my_list if (a - b) in my_list]
    print(diffs)

    return(diffs)


result = find_diffs(pos_e)
# for _ in range(4):
#     result = find_diffs(result)
                        

delta = start - datetime.now()
print(result)
print(f'Duration {delta}')
