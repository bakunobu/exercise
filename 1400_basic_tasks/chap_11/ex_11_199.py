# a
def find_first_neg(nums:list) -> int:
    for i in range(len(nums)):
        if nums[i] < 0:
            return(i)
        

def print_after_first_neg(nums:list) -> None:
    i = find_first_neg(nums)
    print(* nums[i+1:], sep=', ')
    
    
# b
def find_last_neg(nums:list) -> int:
    for i in range(len(nums)-1, -1, -1):
        if nums[i] < 0:
            return(i)
        
        
def print_before_last_neg(nums:list) -> None:
    i = find_last_neg(nums)
    print(* nums[:i], sep=', ')