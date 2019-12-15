#!/usr/bin/env python3

cands = { '파이리': {'code-grade':950, 'code-style':5, 'system-design':3,'potential':5, 'attitude':5, 'portfolio':1},
          '청아': {'code-grade':800, 'code-style':4.5, 'system-design':3,'potential':4, 'attitude':5, 'portfolio':3},
          '혹찬기': {'code-grade':650, 'code-style':3, 'system-design':4,'potential':5, 'attitude':5, 'portfolio':1},
          '킴숙주': {'code-grade':650, 'code-style':2, 'system-design':4,'potential':3, 'attitude':5, 'portfolio':1},
          '이산': {'code-grade':650, 'code-style':2.5, 'system-design':2,'potential':5, 'attitude':5, 'portfolio':1},
          '강산애': {'code-grade':600, 'code-style':2, 'system-design':1,'potential':2, 'attitude':5, 'portfolio':3},
          '준마에': {'code-grade':550, 'code-style':2, 'system-design':3,'potential':5, 'attitude':5, 'portfolio':3},
          '이상준': {'code-grade':450, 'code-style':2, 'system-design':2,'potential':5, 'attitude':5, 'portfolio':4},
          '김국주': {'code-grade':450, 'code-style':3, 'system-design':3.5,'potential':5, 'attitude':5, 'portfolio':5},
          '황산벌': {'code-grade':450, 'code-style':3, 'system-design':3,'potential':5, 'attitude':5, 'portfolio':3.5} }

weights = { 'code-grade': 0.25,
            'code-style': 0.10,
            'potential': 0.30,
            'attitude': 0.20,
            'portfolio': 0.15 }

def main():
    top4 = sort_candidates(cands, weights)[:4]
    residue = sort_candidates(cands, weights)[4:]
    print(top4)
    print()
    print(residue)

def sort_candidates(cands, weights):
    ''' @return [(name, score)] '''
    name_score_lst = [(name, round(calc_score(grades, weights), 2)) for (name, grades) in cands.items()]
    name_score_lst.sort(key=lambda p:p[1], reverse=True)
    return name_score_lst

def calc_score(grades, weights):
    ''' @return (name, score) '''
    score = 0
    for attr, w in weights.items():
        if attr == 'code-grade':
            score += grades[attr] * 5 * w / 950
        else:
            score += grades[attr] * w
    return score

main()
