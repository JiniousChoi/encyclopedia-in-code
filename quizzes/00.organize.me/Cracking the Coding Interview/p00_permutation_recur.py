#>>> joiner( 1, [ 1,2,3]  )
#[ [1, 1], [1, 2], [1, 3] ]

def joiner(ele, list_of_lists):
    result = []
    for each_list in list_of_lists:
        if type(each_list) != list:
            each_list = [each_list]
        new_list = [ele] + each_list
        result.append( new_list )
    
    return result

def getEventTuples(arr, done):
    #ABNORMAL EXCEPTION HANDLER
    if (len(arr) < 1):
        return []
        
    #EXIT PART
    result = []
    if (len(arr) ==1):
        result = []
        for ele in arr[0]:
            if ele in done:
                continue
            result.append(ele)
        return result
    
    #RECURSIVE PART
    #DO NOT CORRUPT (1)done list, and (2)arr list
    for ele in arr[0]:
        if ele in done:
            continue
        done_new = done[:]
        done_new.append(ele)
        result += joiner( ele, getEventTuples(arr[1:], done_new) )
    
    return result

def permutation_wrapper(arr, cnt=None):
    if cnt==None:
        cnt = len(arr)
        
    #if 0< cnt <= len(arr): okay
    if 0 >= cnt or cnt > len(arr):
        return []
        
    arr_dup = []
    for i in range(cnt):
        arr_dup.append(arr)
        
    return getEventTuples( arr_dup, [])
    
if __name__=="__main__":

    arr = [1,2,3,4]
    print permutation_wrapper(arr,4)


