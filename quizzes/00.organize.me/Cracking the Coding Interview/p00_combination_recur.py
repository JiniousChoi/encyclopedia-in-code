#>>> joiner( (0,), [(1,2),(1,3),(2,3)] )
#[(0, 1, 2), (0, 1, 3), (0, 2, 3)]
def joiner(tpl, list_of_tuples):
    result = []
    for each_tuple in list_of_tuples:
        result +=  [tpl + each_tuple]
    
    return result

def combination(arr, start_idx, many):
    if (start_idx<0) or (many <1) or ( start_idx+many>len(arr) ):
        return []
    
    result = []
    
    if many ==1:
        for e in arr[start_idx:]:
            result+= [(e,)]
        return result
    
    #elif many > 1:
    many -= 1
    for e in arr[start_idx:]:
        start_idx += 1
        result += joiner( (e,) , combination(arr, start_idx, many) )
        
    return result

def combination_wrapper(arr, many):
    start_idx = 0
    return combination(arr, start_idx, many)

if __name__=="__main__":
    arr = [1,2,3,4,5,6]
    print combination_wrapper( arr, 1 )
    print combination_wrapper( arr, 2 )
    print combination_wrapper( arr, 3 )
    print combination_wrapper( arr, 4 )
    print combination_wrapper( arr, 5 )
    print combination_wrapper( arr, 6 )
    
#>>>combination_wrapper( [1,2,3,4,5,6] , 3 )
#[(1, 2, 3), (1, 2, 4), (1, 2, 5), (1, 2, 6), (1, 3, 4), (1, 3, 5), (1, 3, 6), (1, 4, 5), (1, 4, 6), (1, 5, 6), (2, 3, 4), (2, 3, 5), (2, 3, 6), (2, 4, 5), (2, 4, 6), (2, 5, 6), (3, 4, 5), (3, 4, 6), (3, 5, 6), (4, 5, 6)]

