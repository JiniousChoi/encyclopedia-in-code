def getCombiForCents_wrapper(change, possible_list):
    result = []
    getCombiForCents(change, possible_list, result)
    return result

def getCombiForCents(change, possible_list, result):
    if not possible_list:
        assert(False)
    
    if len(possible_list) == 1:
        money = possible_list[0]
        max_cnt_float = 1.0 * change / money
        max_cnt_int = change / money
        if max_cnt_float == float(max_cnt_int) :
            result.append([max_cnt_int])
            return True
        else:
            result.append('this should not be printed overall')
            return False

    #presumably len(possible_list) >= 2
    if len(possible_list) < 2:
        assert(False)
        
    money = possible_list[0]
    max_cnt_int = change / money
    #[::-1] to keep in decreasing order
    for cnt in range(max_cnt_int+1)[::-1]:
        sub_result = []
        #YOU SHOULD PASS POSSIBLE_LIST.
        #DO NOT POP IT.
        isSuccess = getCombiForCents(change-money*cnt, possible_list[1:], sub_result)
        if isSuccess:
            result += joiner( cnt, sub_result )
    
    #IF ONE OR MORE SUCCEED, RETURN TRUE.
    if result:
        return True
    #OTHERWISE, RETURN FALSE.
    else:
        return False

#ele: 3
#sub_result = [[5,4],[3,5],[4,7]]
#return = [[3,5,4],[3,3,5],[3,4,7]]
def joiner(ele, sub_result):
    result = []
    
    for each_combi_list in sub_result:
        result.append( [ele]+each_combi_list )
    
    return result

if __name__=="__main__":
    change = 1000
    possible_list = [ 25, 10, 5, 1 ]
    #change = 99
    #possible_list = [ 19, 6 ,7, 17 ]
    print getCombiForCents_wrapper(change, possible_list)
    print len( getCombiForCents_wrapper(change, possible_list) )
    
