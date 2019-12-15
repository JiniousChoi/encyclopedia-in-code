#!/usr/bin/python3
## author: jinchoiseoul@gmail.com


from functools import reduce


def guess_three_daughters_ages():
    prod_of_ages = 72
    triples = list(triple_factors(prod_of_ages))
    triples = filter_triples_for_same_sum(triples)
    triples = filter_triples_with_piano_playable_age(triples)
    return triples


def triple_factors(n, ages=[]):
    ''' yield [age::int] '''
    if len(ages)==3:
        if product(ages)==72 and sum(ages)<=20:
            yield ages[:] #Note: don't forget to yield copied list
        return #Note: don't forget to return here

    # backtracking
    lower_bound = ages[-1] if ages else 1
    for a in range(lower_bound,n+1):
        if n%a==0:
            ages.append(a)
            yield from triple_factors(n//a, ages)
            ages.pop(-1)


def product(ages):
    return reduce(lambda x,acc: x*acc, ages, 1)


def filter_triples_for_same_sum(triples):
    sums = {}
    for triple in triples:
        triple_sum = sum(triple)
        sums.setdefault(triple_sum, [])
        sums[triple_sum].append(triple)

    res = []
    for triple_sum, triple_ls in sums.items():
        if len(triple_ls) >= 2:
            res.extend(triple_ls)
    return res


def filter_triples_with_piano_playable_age(triples):
    return [triple for triple in triples if max(triple) >= 7]


print(guess_three_daughters_ages())
