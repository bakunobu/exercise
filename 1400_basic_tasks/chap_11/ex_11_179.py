def manual_sort(results:list) -> list:
    i = 0
    result = results.pop(0)
    while i < len(results) - 1:
        if result > results[i]:
            i += 1
        else:
            results.insert(i, result)
            return(results)
    results.append(result)
    return(results)