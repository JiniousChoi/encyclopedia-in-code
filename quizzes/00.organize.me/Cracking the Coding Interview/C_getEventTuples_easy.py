#>>> joiner( 1, [ 1,2,3]  )
#[(1, 1), (1, 2), (1, 3)]

def joiner(ele, list_of_lists):
    result = []
    for each_list in list_of_lists:
        if type(each_list) != list:
            each_list = [each_list]
        new_list = [ele] + each_list
        result.append( new_list )
    
    return result

def getEventTuples(arr):
    if (len(arr) < 1):
        return []
        
    result = []
    
    if (len(arr) ==1):
        return arr[0]
    
    for ele in arr[0]:
        result += joiner( ele, getEventTuples(arr[1:]) )
    
    return result
    
if __name__=="__main__":

    arr_new = [ ['a','b'],[1,2,3],[1,2,3] ]
    print getEventTuples( arr_new )

#>>>print getEventTuples( [ ['a','b'],[1,2,3],[1,2,3] ] )
#[['a', 1, 1], ['a', 1, 2], ['a', 1, 3], ['a', 2, 1], ['a', 2, 2], ['a', 2, 3], ['a', 3, 1], ['a', 3, 2], ['a', 3, 3], ['b', 1, 1], ['b', 1, 2], ['b', 1, 3], ['b', 2, 1], ['b', 2, 2], ['b', 2, 3], ['b', 3, 1], ['b', 3, 2], ['b', 3, 3]]
