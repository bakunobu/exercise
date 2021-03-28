def eucl_gcd(a:int, b:int) -> int:
    while b != 0:
        a, b = max(a, b), min(a, b)
        a, b = b, a % b
    return(a)
        
        
def gcd_of_three(a:int, b:int, c:int) -> int:
    d = eucl_gcd(a, b)
    return(eucl_gcd(c, d))