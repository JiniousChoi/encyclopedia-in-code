'''
this should function the same as from itertools.product
'''

def product(*lists):
    for ls in lists:
        assert len(ls)>0
    idx_list = [0]*len(lists)
    len_list = [len(ls) for ls in lists]
    while True:
        val_list = []
        # ex) idx_list = [0,1,0]
        for i,idx in enumerate(idx_list):
            val_list.append(lists[i][idx])
        yield val_list
        try:
            idx_list = add_one(len_list, idx_list)
        except ValueError:
            break

def add_one(radix_list, idx_list):
    #pre-assertion
    assert len(radix_list) == len(idx_list)
    if radix_list==[idx+1 for idx in idx_list]:
        raise ValueError

    for i, val in enumerate(idx_list):
        assert radix_list[i] > val

    #logic
    idx_list[-1]+=1
    for digit in range(len(idx_list))[::-1]:
        if idx_list[digit] == radix_list[digit]:
            #transactional
            idx_list[digit-1] += 1
            idx_list[digit] = 0
        else:
            break
    
    #post-assertion
    for i, val in enumerate(idx_list):
        assert radix_list[i] > val

    return idx_list

if __name__=="__main__":
    print('implemented_product')
    #for each in product('ㄱㄴㄷ','abc','123'):
    #    print(each)

    result = product('ㄱㄴㄷ','abc','123')
    while True:
        print(next(result))
