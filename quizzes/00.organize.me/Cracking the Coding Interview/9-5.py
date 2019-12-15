'''
9.5-주어진 문자열의 모든 순열을 찾는 메소드를 작성하라.
'''
def permutation(li):
    assert isinstance(li, list)
    if len(li)==1:
        return li
    elif len(li)==2:
        return [[li[0],li[1]], [li[1],li[0]]]
    for i in range(len(li)):
        new_li = circular(i, li)
        f, r = new_li[0], new_li[1:]
        for each in permutation(r):
            each.insert(0,f)
            print(each)

def circular(i, li):
    assert i<=len(li)-1
    result = []
    for j in range(len(li)):
        result.append( li[(i+j)%len(li)] )
    return result
    
li = ['a','b','c']
permutation(li)
