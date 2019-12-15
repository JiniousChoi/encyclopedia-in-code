def quicksort_decr_wrapper(arr):
    quicksort_decr( arr, 0, len(arr)-1 )

def quicksort_decr(arr, start_idx, end_idx):
    #arr has no element
    if end_idx - start_idx < 0:
        return
        
    #arr has 1 element
    elif end_idx - start_idx == 0:
        #practically sorted
        return
        
    #arr has 2 elements
    #actually, this may not be essential!!!
    #BUT more efficient this way than calling quicksort for an array of
    #only two elements
    elif end_idx - start_idx == 1:
        if arr[start_idx] < arr[end_idx]:
            arr[start_idx], arr[end_idx] = arr[end_idx], arr[start_idx]
        return
    
    #From this part, arr has more than 3 elements
    #Initialize variables
    the_idx = start_idx
    the_val = arr[start_idx]
    p = start_idx + 1
    q = end_idx
    
    ###
    ###part1: bi-parting the given arr against pivot value
    ###
    while p < q :
        if arr[p] >= the_val >= arr[q]:
            p+=1
            q-=1
        
        #right p, wrong q
        elif arr[p] >= the_val and the_val < arr[q] :
            p+=1
        
        #wrong p, right q
        elif arr[p] < the_val and the_val >= arr[q]:
            q-=1
            
        #both wrong
        elif arr[p] < the_val < arr[q]:
            arr[p], arr[q] = arr[q], arr[p]
            p+=1
            p-=1
            
        #to minimize logical bug
        else:
            print the_val, arr[p],  arr[q]
            assert(False)
        
    ###
    ###part2: put pivot value in between the bi-parts
    ###
    # case1: completely bi-parted 
    if q + 1 == p:
        arr[the_idx], arr[q] = arr[q], arr[the_idx]
        the_idx = q
        
    # case2: arr[p] element should be sorted
    elif p == q:
        if  the_val <= arr[p]:
            arr[the_idx], arr[p] = arr[p], arr[the_idx]
            the_idx = p
        else:
            arr[the_idx], arr[p-1] = arr[p-1], arr[the_idx]
            the_idx = p-1
        
    else:
        assert(False)

    quicksort_decr( arr, start_idx, the_idx-1 )
    quicksort_decr( arr, the_idx+1, end_idx )
        
if __name__=='__main__':
    print 'testcase'
    from random import randint
    testcases = []
    minCnt, maxCnt = 10, 15
    minInt, maxInt=-10, 10
    
    for i in range(5):
        testcases.append([])
        for j in range(randint( minCnt, maxCnt )):
            testcases[i].append( randint( minInt, maxInt ) )
    
    for testcase in testcases:
        print testcase, '->',
        quicksort_decr_wrapper(testcase)
        print testcase
