def list_rorator(any_list:list) -> list:
    start_el = any_list.pop(0)
    any_list.append(start_el)
    return(any_list)


"""
new_list = [1,2,3,4,5]

for i in range(3):
    new_list = list_rorator(new_list)
    
print(new_list)
"""