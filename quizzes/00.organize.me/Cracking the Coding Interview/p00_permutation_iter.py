def permutation(arr, many):
    
    result = []
    queue = []
    for ele in arr:
        queue.append([ele])
    
    while( 0<len(queue) ):
        cur_list=queue.pop(0)
        
        if len(cur_list) < many:
            for ele in arr:
                if ele not in cur_list:
                    tmp_list = cur_list[:]
                    tmp_list.append(ele)
                    queue.append(tmp_list)
        
        elif len(cur_list) == many:
            result.append(cur_list)
            
        else:
            assert(False)
    
    return result

if __name__=="__main__":

    arr = [1,2,3,4]
    print permutation(arr,4)

