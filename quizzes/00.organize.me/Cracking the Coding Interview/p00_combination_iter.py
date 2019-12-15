def combination_iter(arr, many):
    if type(arr)!=list or many<0 or many>len(arr):
        assert(False)
    
    result = []
    queue = []
    for ele in arr:
        queue.append([ele])
    
    while(0<len(queue)):
        cur_list = queue.pop(0)
        
        if len(cur_list) < many:
            for ele in arr:
                if cur_list[-1] < ele:
                    tmp_list = cur_list[:]
                    tmp_list.append(ele)
                    queue.append(tmp_list)
                
        elif len(cur_list) == many:
            result.append( cur_list )
        else:
            assert(False)
    
    return result
    
def combination_wrapper( arr, many ):
    #if not monotonically increasing:
    #exit
    for i in range(len(arr))[:-1]:
        if arr[i]>arr[i+1]:
            assert(False)
    #if monotonically increasing:
    return combination_iter(arr,many)
if __name__=="__main__":
    arr = [1,2,3,4,5,6]
    print combination_wrapper( arr, 1 )
    print combination_wrapper( arr, 2 )
    print combination_wrapper( arr, 3 )
    print combination_wrapper( arr, 4 )
    print combination_wrapper( arr, 5 )
    print combination_wrapper( arr, 6 )
 
