import math


# a
def sin_div(n:int) -> float:
    if n == 1:
        return(math.sin(1))
    else:
        return(math.sin(n) + math.sin(n-1))
    

def part_sum(n:int):
    total = 0
    for x in range(1, n+1):
        total += 1 / sin_div(x)
    return(total)


# b
class SqrtTwo:
    def __init__(self, n:int) -> None:
        self.n = n
    
    
    def sqrt_two(self, n=None) -> float:
        if n is None:
            n = self.n
        if n == 1:
            return(math.sqrt(2))
        else:
            return(math.sqrt(2 + self.sqrt_two(n-1)))
    
c = SqrtTwo(20)
print(c.sqrt_two())

# c
def sin_div(n:int) -> float:
    if n == 1:
        return(math.sin(1))
    else:
        return(math.sin(n) + math.sin(n-1))


def cos_div(n:int) -> float:
    if n == 1:
        return(math.cos(1))
    else:
        return(math.cos(n) + math.cos(n-1))  
    

def part_sum(n):
    total = 0
    for x in range(1, n+1):
        total += cos_div(x) / sin_div(x)
    return(total)


# d
class SqrtProdSum:
    def __init__(self, n:int) -> None:
        self.n = n
    
    
    def sqrt_prod_sum(self, n=None) -> float:
        if n is None:
            n = self.n
        if n == 1:
            return(math.sqrt(3 * n))
        else:
            return(math.sqrt(3 * n) + self.sqrt_prod_sum(n-1))
        
        
c = SqrtProdSum(20)
print(c.sqrt_prod_sum())