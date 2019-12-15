def getCombiForCents_wrapper(possible_list, mini, maxi=None):
    if not maxi:
        maxi = (mini-1)+max(possible_list)
    
    return getCombiForCents(possible_list, mini, maxi)

def getCombiForCents(possible_list, mini, maxi):
    if not possible_list:
        assert(False)
    
    result = []
    queue = []
    init_list = []
    
    for i in range(len(possible_list)):
        init_list.append(0)
    #init_list = [0,0,0,0]
    
    for i, price in enumerate(possible_list):
        if price <=maxi:
            tmp_init_list = init_list[:]
            tmp_init_list[i] +=1
            queue.append(tmp_init_list)
            
    #queue INVARIANT:
    #In queue are EVERY POSSIBLE combinations less than maxi
    while( 0<len(queue) ):
        #dup_test(queue)
        #print len(queue)
        #print queue
        cur_price_list = queue.pop(0)
        cur_price_tot = list_product(possible_list, cur_price_list)
        
        # if mini <= cur_price_tot <= maxi:
        if mini <= cur_price_tot:
            result.append(cur_price_list)
        #pdb.set_trace()
        #DO NOT CORRUPT cur_price_list for sibling operations
        for i, add_price in enumerate(possible_list):
            if (cur_price_tot+add_price) <= maxi:
                new_price_list = cur_price_list[:]
                new_price_list[i] += 1
                #CHECK IF new_price_list is already in queue:
                #WITHOUT MEMBERSHIP TEST, INFINITE LOOPING MIGHT HAPPEN.
                #queue.append(new_price_list)
                if new_price_list not in queue:
                    queue.append(new_price_list)
                
    #end of while:
    #queue is empty
    #result is full of adequate list of combinations
    return result

def list_product(list1, list2):
    if len(list1) != len(list2):
        assert(False)
    sum = 0
    for i in range(len(list1)):
        sum += list1[i]*list2[i]

    return sum

def dup_test(queue):
    queue_len = len(queue)
    for i in range(queue_len)[:-1:]:
        for j in range(queue_len)[i+1::]:
            if queue[i] == queue[j]:
                print 'oh no:',(i, j), len(queue), queue[i]
                #assert(False)
    
def test1():
    mini = 1000
    maxi = 1000
    possible_list = [ 25, 10, 5, 1 ]
    #change = 99
    #possible_list = [ 19, 6 ,7, 17 ]
    result = getCombiForCents_wrapper(possible_list, mini, maxi)
    print result
    print len(result)
    
if __name__=="__main__":
    #print list_product([3,4,5],[1,2,1])
    import pdb
    test1()
    #dup_test([1,2,3,9,5,6,7,8,9])



