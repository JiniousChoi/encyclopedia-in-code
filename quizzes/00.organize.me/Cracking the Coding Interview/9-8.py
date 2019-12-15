'''
9.8 - 쿼터, 다임, 니켈, 페니가 무한히 주어졌을 때, n센트를 표현하는 경우의 수
절차적, 재귀적 구현 완료
'''
def coin_procedural(n):
    result=[]
    for q in range(n//25+1):
        left1=n-q*25
        for d in range(left1//10+1):
            left2=left1-d*10
            for ni in range(left2//5+1):
                pe=left2-ni*5
                result.append([q,d,ni,pe])
    return result

#print(coin_procedural(100))

def coin_recursive(n, coin_types, coin_index):
    assert n>=0
    assert 0<=coin_index<len(coin_types)

    cur_coin = coin_types[coin_index]
    if coin_index==len(coin_types)-1:
        return [[n//cur_coin]]

    tmp = []
    for cnt in range(n//cur_coin+1):
        for each in coin_recursive(n-cur_coin*cnt, coin_types, coin_index+1):
            each.insert(0, cnt)
            tmp.append(each)
    return tmp

def coin_recursive_wrapper(n):
    return coin_recursive(n, [25,10,5,1], 0)

print(coin_recursive_wrapper(100))
