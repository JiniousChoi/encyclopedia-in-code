#!/usr/bin/python3

'''
This script is to make one-paged printer to function as two-sided.
'''

def pages_in_order(tot_pages, per_each_page):
    assert tot_pages>=2, "pages_in_order::assert tot_pages>=2"
    assert per_each_page >= 1, "pages_in_order::assert per_each_page>=1"
    fp = _first_pages(tot_pages, per_each_page)
    sp = _second_pages(tot_pages, per_each_page)
    return (fp, sp)


def _first_pages(tot_pages, per_each_page):
    n, p = tot_pages, per_each_page
    paired = _pairing(n, p)
    odd = _taking_odd(paired)
    flattened = _flattening(odd)
    return flattened
    #return [x for x in range(1,n+1) if x%2==1]


def _second_pages(tot_pages, per_each_page):
    n, p = tot_pages, per_each_page
    paired = _pairing(n, p)
    reversed_even = reversed(_taking_even(paired))
    flattened = _flattening(reversed_even)
    return flattened


def _pairing(tot_pages, per_each_page):
    n, p = tot_pages, per_each_page
    #return [list(range(x-p+1,x+1)) for x in range(1,n+1) if x%p==0]
    outter = []
    inner = []
    for x in range(1, n+1):
        inner.append(x)
        if(len(inner) == p):
            outter.append(inner)
            inner = []
    if(len(inner)>0):
        outter.append(inner)
        inner = []

    return outter
        
        
def _taking_odd(paired):
    return [l for (i,l) in enumerate(paired) if (i+1)%2]


def _taking_even(paired):
    return [l for (i,l) in enumerate(paired) if (i+1)%2==0]
    

def _flattening(second_order_list):
    ll = second_order_list
    flattened = []
    for l in ll:
        flattened.extend(l)
    return flattened


if __name__ == "__main__":
    #testing
    print((5,1), ":", pages_in_order(5,1))
    print((5,2), ":", pages_in_order(5,2))
    print((5,4), ":", pages_in_order(5,4))
    print((7,2), ":", pages_in_order(7,2))
    print((7,4), ":", pages_in_order(7,4))
    print((8,4), ":", pages_in_order(8,4))

