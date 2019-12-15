#!/usr/bin/python3
#-*- coding: utf-8 -*-
'''
9-6
n이 주어졌을 때 n-쌍의 괄호로 만들 수 있는 모든 합당한 조합(괄호가 적절히 열리고 닫힌)을 출력하는 알고리즘을 구현하라.
'''
def _parenthesis(opening, closing):
    assert opening>=0 and closing >=0
    if opening==0 and closing==0:
        return [[]]
    tmp = []
    if openable(opening, closing):
        for sub in _parenthesis(opening-1, closing):
            sub.insert(0,'(')
            tmp.append(sub)
    if closable(opening, closing):
        for sub in _parenthesis(opening, closing-1):
            sub.insert(0,')')
            tmp.append(sub)
    return tmp

def openable(opening, closing):
    '''
    opening: 남은 열림괄호의 수
    '''
    assert opening >=0 and closing >=0
    if opening > 0:
        return True
    else:
        return False

def closable(opening, closing):
    '''
    3,3일경우 불가능/ 2,3일경우
    '''
    assert opening >=0 and closing >=0
    assert opening <= closing
    if opening == closing:
        return False
    if opening < closing:
        return True

def parenthesis(how_many):
    return _parenthesis(how_many, how_many)

for each_case in parenthesis(3):
    print(''.join(each_case))
