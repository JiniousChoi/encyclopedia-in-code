#!/usr/bin/python3
'''
9-6
n이 주어졌을 때 n-쌍의 괄호로 만들 수 있는 모든 합당한 조합
(괄호가 적절히 열리고 닫힌)을 출력하는 알고리즘을 구현하라.
'''

def command(*arg):
    print(*arg)


def parenthesis(p, o, c):
    assert o>=0 and c>=0
    
    if o==0 and c==0:
        command(p)
        return

    if o>0: 
        parenthesis(p+'(', o-1, c)

    if c>0 and o<c:
        parenthesis(p+')', o, c-1)

if __name__=="__main__":
    parenthesis('', 3, 3)
