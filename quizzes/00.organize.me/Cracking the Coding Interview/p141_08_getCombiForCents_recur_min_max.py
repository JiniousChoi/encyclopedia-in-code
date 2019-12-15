from math import ceil, floor
def getCombiForCents_wrapper(possible_list, range_from, range_to=None):
    if range_to == None:
        minimum_int_unit = 1
        range_to = range_from+max(possible_list) - minimum_int_unit
    spent = 0
    result = getCombiForCents(spent, possible_list, range_from, range_to)
    return result

def getCombiForCents(spent, possible_list, range_from, range_to):
    #ABNORMAL VARIABLE VALUES:
    if not possible_list or not(spent<=range_to) or spent<0 or range_from<0 or range_to<0:
        assert(False)
    
    #INITIALIZE VARIABLES:
    result = []

    #END OF RECURSION PART
    if len(possible_list) == 1:
        money = possible_list[0]
        #INVARIANT: 0 <= spent <= range_from <= range_to
        #INVARIANT: 0 <= (range_from - spent)/ money
        #INVARIANT: 0 <= (range_to - spent)/money
        cnt_from_float = 1.0*(range_from - spent) / money
        cnt_to_float = 1.0*(range_to - spent) / money
        
        cnt_from_int = int(ceil(cnt_from_float))
        if cnt_from_int <0:
            cnt_from_int = 0
        cnt_to_int = int(floor(cnt_to_float))
        
        for cnt in range(cnt_from_int, cnt_to_int +1)[::-1]:
            #INVARIANT: EVERY cnt SATISFIES "range_from <= spent+cnt <= range_to":
                result.append([cnt])
        
        return result
    
    #presumably len(possible_list) >= 2
    if len(possible_list) < 2:
        assert(False)
        
    money = possible_list[0]
    change = range_to - spent
    max_cnt_int = change / money
    
    #[::-1] to keep in decreasing order
    for cnt in range(max_cnt_int+1)[::-1]:
        #DO NOT CORRUPT (1)possible_list, (2)spent
        sibling_result = getCombiForCents(spent+cnt*money, possible_list[1:], range_from, range_to)
        result += joiner( cnt, sibling_result )

    #COME BACK UP FROM DEPTHRETURN    
    return result

#ele: 3
#sibling_result = [[5,4],[3,5],[4,7]]
#return = [[3,5,4],[3,3,5],[3,4,7]]
def joiner(ele, sibling_result):
    result = []
    
    for each_combi_list in sibling_result:
        result.append( [ele]+each_combi_list )
    
    return result

if __name__=="__main__":
    range_from = 100
    range_to = 103
    possible_list = [ 25, 10, 5, 1 ]
    
    #change = 99
    #possible_list = [ 19, 6 ,7, 17 ]
    
    result = getCombiForCents_wrapper(possible_list, range_from, range_to)
    print result, len(result)
    
