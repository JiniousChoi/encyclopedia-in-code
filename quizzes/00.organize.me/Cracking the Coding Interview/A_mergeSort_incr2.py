#A_mergeSort_incr_wrapper keeps its original arr list intact. It returns result list.
#A_mergeSort_incr2_wrapper returns nothing. It changes the original arr list.
#I prefer the first one because it keeps its original arr intact

def mergeSort_incr_wrapper(arr):
    return mergeSort_incr( arr, 0, len(arr)-1 )

def mergeSort_incr(arr, start_idx, end_idx):
    if start_idx > end_idx:
        return
    
    elif start_idx == end_idx:
        return
    
    mid_idx = (start_idx+end_idx) / 2
    mergeSort_incr( arr, start_idx, mid_idx )
    mergeSort_incr( arr, mid_idx+1, end_idx )
    
    mergeTwoParts_incr( arr, start_idx, mid_idx, end_idx )

def mergeTwoParts_incr( arr, start_idx, mid_idx, end_idx ):
    result = []
    part1_cur_idx = start_idx
    part1_end_idx = mid_idx
    part2_cur_idx = mid_idx+1
    part2_end_idx = end_idx
    
    #arr is used!!!
    while part1_cur_idx<=part1_end_idx and part2_cur_idx<=part2_end_idx :
        if arr[part1_cur_idx] == arr[part2_cur_idx]:
            result.append( arr[part1_cur_idx] )
            result.append( arr[part2_cur_idx] )
            part1_cur_idx += 1
            part2_cur_idx += 1

        elif arr[part1_cur_idx] < arr[part2_cur_idx]:
            result.append( arr[part1_cur_idx] )
            part1_cur_idx += 1
            
        elif arr[part1_cur_idx] > arr[part2_cur_idx]:
            result.append( arr[part2_cur_idx] )
            part2_cur_idx += 1
            
        else:
            print 'this should not occur'
            assert(False)
    
    if part1_cur_idx <= part1_end_idx:
        result.extend( arr[part1_cur_idx:part1_end_idx+1] )

    elif part2_cur_idx <= part2_end_idx:
        result.extend( arr[part2_cur_idx:part2_end_idx+1] )

    #update arr
    arr[start_idx : end_idx+1] = result

def isIncremental(arr):
    for i in range( len(arr)-1 ):
        if arr[i] > arr[i+1]:
            return False
    return True
        
if __name__ == "__main__":
    from random import randint
    testcaseCnt = 5
    minCnt, maxCnt = 10, 30
    minInt, maxInt = -10, 100
    
    testcases = []
    for i in range(testcaseCnt):
        testcases.append([])
        for j in range( randint(minCnt, maxCnt) ):
            testcases[i].append( randint(minInt, maxInt) )
    
    for testcase in testcases:
        print testcase, '->',
        beforeLen = len(testcase)
        mergeSort_incr_wrapper(testcase)
        print testcase
        afterLen = len(testcase)
        if beforeLen == afterLen:
            print 'lengths match'
        else:
            assert(False)
            
        if isIncremental(testcase):
            print 'incremental'
        else:
            assert(False)

        print ''
