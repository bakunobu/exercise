def man_sort(speed:list, k:int) ->list:
    k -= 1
    temp = speed.pop(k)
    if temp < speed[k-1]:
        i = k - 2
        while i > 0:
            if temp > speed[i]:
                speed.insert(i+1, temp)
                return(speed)
            else:
                i -= 1
        speed.insert(0, temp)
    else:
        i = k + 1
        while i < len(speed):
            if temp < speed[i]:
                speed.insert(i, temp)
                return(speed)
            else:
                i += 1
        speed.append(temp)
        
    return(speed) 