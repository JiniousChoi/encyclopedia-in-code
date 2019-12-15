# -*- coding:utf-8 -*-

def mergeSort_wrapper(arr, compare):
    return mergeSort( arr, 0, len(arr)-1, compare )

def mergeSort(arr, start_idx, end_idx, compare):
    if start_idx > end_idx:
        return
    
    elif start_idx == end_idx:
        return
    
    mid_idx = (start_idx+end_idx) / 2
    mergeSort( arr, start_idx, mid_idx, compare )
    mergeSort( arr, mid_idx+1, end_idx, compare )
    
    mergeTwoParts( arr, start_idx, mid_idx, end_idx, compare)

def mergeTwoParts( arr, start_idx, mid_idx, end_idx, compare ):
    result = []
    part1_cur_idx = start_idx
    part1_end_idx = mid_idx
    part2_cur_idx = mid_idx+1
    part2_end_idx = end_idx
    
    #arr is used!!!
    while part1_cur_idx<=part1_end_idx and part2_cur_idx<=part2_end_idx :
        if compare(arr[part1_cur_idx], arr[part2_cur_idx]) ==0:
            result.append( arr[part1_cur_idx] )
            result.append( arr[part2_cur_idx] )
            part1_cur_idx += 1
            part2_cur_idx += 1

        elif compare(arr[part1_cur_idx], arr[part2_cur_idx]) <0:
            result.append( arr[part1_cur_idx] )
            part1_cur_idx += 1
            
        elif compare(arr[part1_cur_idx], arr[part2_cur_idx]) >0:
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

#callback fn definitions
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
        mergeSort_wrapper(testcase, compare_str_decr)
        print testcase
        
