# -*- coding:utf-8 -*-

def quicksort_wrapper(arr, compare):
    quicksort ( arr, 0, len(arr)-1, compare)

def quicksort(arr, start_idx, end_idx, compare):
    #arr has no element
    if end_idx - start_idx < 0:
        return
    
    #this part is not necessary.
    #it just prevent one more needless recursive in-step
    #arr has 1 element
    elif end_idx - start_idx == 0:
        #practically sorted
        return
        
    #From this part, arr has more than 2 elements
    #Initialize variables
    the_idx = start_idx
    the_val = arr[start_idx]
    p = start_idx + 1
    q = end_idx
    
    ###
    ###part1: bi-parting the given arr against pivot value
    ###
    while p < q :
        #if arr[p] <= the_val <= arr[q]:
        if (compare(arr[p], the_val)<=0) and (compare(the_val,arr[q])<=0):
            p+=1
            q-=1
        
        #right p, wrong q
        #elif arr[p] <= the_val and the_val > arr[q] :
        elif (compare(arr[p], the_val)<=0) and (compare(the_val,arr[q])>0):
            p+=1
        
        #wrong p, right q
        #elif arr[p] > the_val and the_val <= arr[q]:
        elif (compare(arr[p], the_val)>0) and (compare(the_val,arr[q])<=0):
            q-=1
            
        #both wrong
        #elif arr[p] > the_val > arr[q]:
        elif (compare(arr[p], the_val)>0) and (compare(the_val,arr[q])>0):
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
        
        #part1_start_idx = start_idx
        #part1_end_idx = q-1
        ## pivot_dix == q
        #part2_start_idx = p
        #part2_end_idx = end_idx
        
    # case2: arr[p] element should be sorted
    elif p == q:
        #if  the_val >= arr[p]:
        if compare(the_val, arr[p])>=0:
            arr[the_idx], arr[p] = arr[p], arr[the_idx]
            the_idx = p
        else:
            arr[the_idx], arr[p-1] = arr[p-1], arr[the_idx]
            the_idx = p-1
        
    else:
        assert(False)

    quicksort( arr, start_idx, the_idx-1, compare )
    quicksort( arr, the_idx+1, end_idx, compare )

from random import randint

def int_testcases_generator(minCnt=10, maxCnt=150, minInt=-10, maxInt=10):
    print 'int_testcases_generator called'

    testcases = []
    
    for i in range(5):
        testcases.append([])
        for j in range(randint( minCnt, maxCnt )):
            testcases[i].append( randint( minInt, maxInt ) )
    return testcases

def str_testcases_generator(wordsMinCnt=10, wordsMaxCnt=10, charMinCnt=5, charMaxCnt=10):
    sample_str= 'ABCDEFGHIJKLMNOPQRSTUVWXYZ!abcdefghijklmnopqrstuvwxyz'
    sample_str_len=len(sample_str)
    
    testcases=[]
    set_count = 5
    
    for i in range(set_count):
        testcases.append([])
        
    for testcase in testcases:
        for word_cnt in range(randint(wordsMinCnt, wordsMaxCnt)):
            temp_str=''
            for char_cnt in range(randint(charMinCnt, charMaxCnt)):
                sample_ch = sample_str[randint(0,sample_str_len-1)]
                temp_str += sample_ch
            testcase.append(temp_str)

    return testcases

#callback functions definitions
def compare_int_incr(a,b):
    return a-b

def compare_int_decr(a,b):
    return compare_int_incr(b,a)
    
def compare_strlen_incr(s1,s2):
    return len(s2)-len(s1)
    
def compare_strlen_decr(s1,s2):
    return compare_strlen_incr(s1,s2)

def compare_str_incr(s1,s2):
    if s1>s2: return 1
    elif s1==s2: return 0
    else: return -1

def compare_str_decr(s1,s2):
    return compare_str_incr(s2,s1)

if __name__=='__main__':
    
    #testcases = int_testcases_generator(10, 10, -10, 10)
    testcases = str_testcases_generator(10, 10, 10, 10)
    
    for testcase in testcases:
        print testcase, '->',
        quicksort_wrapper(testcase, compare_str_decr)
        print testcase
