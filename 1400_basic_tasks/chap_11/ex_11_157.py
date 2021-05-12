def del_k_el(nums:list, k:int) -> list:
    del nums[k]
    return(nums)


def get_product_ind(msg:str) -> int:
    while 1:
        try:
            n = int(input(msg))
            return(n)
        except ValueError:
            print('Используйте только целые числа!')
            
def del_prod(prices:list) -> list:
    msg = 'Укажите индекс товара, который необходимо удалить: '
    n = get_product_ind(msg)
    prices = del_k_el(prices, n)
    return(prices)
    