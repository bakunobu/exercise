def count_value(a:int, b:int, c:int,
                d:int, e:int, f:int,
                g:int, h:int, i:int,
                j:int) -> int:
    return(a+2*b+3*c+5*d+10*e+12*f+14*g+15*h+20*i+30*j)

def count_vars(v:int) -> int:
    v = v // 100
    counter = 0
    for a in range(0, v // 1 + 1):
        for b in range(0, v // 2 + 1):
            for c in range(0, v // 3 + 1):
                for d in range(0, v // 5 + 1):
                    for e in range(0, v // 10 + 1):
                        for f in range(0, v // 12 + 1):
                            for g in range(0, v // 14 + 1):
                                for h in range(0, v // 15 + 1):
                                    for i in range(0, v // 20 + 1):
                                        for j in range(0, v // 30 + 1):

                                            if count_value(a,b,c,d,e,f,g,h,i,j) == v:
                                                
                                                counter += 1
    return(counter)


print(count_vars(3000))