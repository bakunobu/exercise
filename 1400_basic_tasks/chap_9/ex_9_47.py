from typing import Union

def simple_eq(a:int, b:int, c:int) -> Union[int, float]:
    return(10 * a + 5 * b + 0.5 * c)


def old_task() -> tuple:
    for a in range(0, 10):
        for b in range(0, 20):
            for c in range(0, 200):
                if a+b+c==100 and simple_eq(a,b,c)==100:
                    return(a, b, c)
                
                
print(old_task())