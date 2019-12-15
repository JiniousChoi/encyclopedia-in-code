def stairways_recur(n_step):
    if n_step < 1:
        return []

    elif n_step == 1:
        return [[1]]
    
    result = []
    result1 = joiner( 1, stairways_recur(n_step-1) )
    result2 = joiner( 2, stairways_recur(n_step-2) )
    result3 = joiner( 3, stairways_recur(n_step-3) )
    
    result = result1 + result2 + result3
    return result

def joiner(ele, double_list):
    result = []
    
    for single_list in double_list:
        result.append( [ele] + single_list[:] )

    return result

if __name__ == "__main__":
    result = stairways_recur(10)
    print result
    print len(result)
