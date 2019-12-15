#A_mergeSort_decr_wrapper keeps its original arr list intact. It returns result list.
#A_mergeSort_decr2_wrapper returns nothing. It changes the original arr list.
#I prefer the first one because it keeps its original arr intact

def mergeSort_incr_wrapper(arr):
    return mergeSort_incr( arr, 0, len(arr)-1 )

def mergeSort_incr(arr, start_idx, end_idx):
    if start_idx > end_idx:
        return
    
    elif start_idx == end_idx:
        return [ arr[start_idx] ]
    
    mid_idx = (start_idx+end_idx) / 2
    part1 = mergeSort_incr( arr, start_idx, mid_idx )
    part2 = mergeSort_incr( arr, mid_idx+1, end_idx )
    
    result = []
    part1_cur_idx = 0
    part2_cur_idx = 0
    
    #no arr is used from now on
    #ONLY part1 and part2 and result are used
    while part1_cur_idx<len(part1) and part2_cur_idx<len(part2) :
        if part1[part1_cur_idx] == part2[part2_cur_idx]:
            result.append( part1[part1_cur_idx] )
            result.append( part2[part2_cur_idx] )
            part1_cur_idx += 1
            part2_cur_idx += 1

        elif part1[part1_cur_idx] < part2[part2_cur_idx]:
            result.append( part1[part1_cur_idx] )
            part1_cur_idx += 1
            
        elif part1[part1_cur_idx] > part2[part2_cur_idx]:
            result.append( part2[part2_cur_idx] )
            part2_cur_idx += 1
            
        else:
            print 'this should not occur'
            assert(False)
    
    if part1_cur_idx < len(part1):
        result.extend( part1[part1_cur_idx:] )
        #test part
        if part2_cur_idx < len(part2):
            print 'this should not happen'
            assert(False)

    elif part2_cur_idx < len(part2):
        result.extend( part2[part2_cur_idx:] )
    
    return result
    
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
        testcase_sorted = mergeSort_incr_wrapper(testcase)
        print testcase, '->', testcase_sorted 

        if len(testcase) == len(testcase_sorted):
            print 'lengths match'
        else:
            assert(False)
            
        if isIncremental(testcase_sorted):
            print 'decremental'
        else:
            assert(False)
