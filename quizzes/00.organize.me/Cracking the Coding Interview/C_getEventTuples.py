#>>> joiner( (1,), [(1,),(2,),(3,) ]  )
#[(1, 1), (1, 2), (1, 3)]

#HARD WAY TO IMPLEMENT

def joiner(tpl, list_of_tuples):
    result = []
    for each_tuple in list_of_tuples:
        result +=  [tpl + each_tuple]
    
    return result

def foo(arr):
    if (len(arr) < 1):
        return []
        
    result = []
    
    if (len(arr) ==1):
        return arr[0]
    
    for tpl in arr[0]:
        result += joiner( tpl, foo(arr[1:]) )
    
    return result
    
def foo_wrapper(arr):
    result = []
    for tpl in arr:
        tpl_new = []
        for ele in tpl:
            tpl_new.append( (ele,) )
        result.append( tpl_new )

    return foo(result)

if __name__=="__main__":
    #arr = [ [('a',),('b',)] , [(1,),(2,),(3,)] , [(1,),(2,),(3,)] ]
    #arr = [ [(1,),(2,),(3,)] , [(1,),(2,),(3,)] ]
    
    #arr_new = [ (1,2,3), (1,2,3) ] #this is okay too.
    arr_new = [ [1,2,3], [1,2,3] ]
    print foo_wrapper( arr_new )


