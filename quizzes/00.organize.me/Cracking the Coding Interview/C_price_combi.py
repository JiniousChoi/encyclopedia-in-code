# -*- coding: utf8 -*-
#열혈강의 page 249 도전 프로그래밍1 도전4 
from C_getEventTuples_easy import getEventTuples


def foo(change, *tuple_of_prices):
    
    cnt_range_list = []
    for price_each in tuple_of_prices:
        max_cnt_each = (change / price_each) + 1
        max_cnt_each_range = range(max_cnt_each)
        cnt_range_list.append( max_cnt_each_range )
    
    cnt_event_list_of_tuples = getEventTuples(cnt_range_list)
    ###
    print cnt_event_list_of_tuples
    
    possible_combi_list = []
    
    
    for cnt_each_tuple in cnt_event_list_of_tuples:
        total_price=0
        for i in range(len(tuple_of_prices)):
            price = tuple_of_prices[i]
            cnt = cnt_each_tuple[i]
            total_price += price*cnt
        if total_price == change:
            possible_combi_list.append(cnt_each_tuple)
    
    return possible_combi_list

#Note: iterate the list of tuples backwards not to disturb indexes of tuples
def foo2(possible_combi_list):
    for i in range( len(possible_combi_list) )[::-1]:
        if 0 in possible_combi_list[i]:
            possible_combi_list.pop(i)

    return possible_combi_list

if __name__=="__main__":
    change = 3500
    price_bread=500
    price_snack=700
    price_coke=400    

    combination = foo(change, price_bread, price_snack, price_coke)
    print combination

    combination2 = foo2(combination)
    print combination2
