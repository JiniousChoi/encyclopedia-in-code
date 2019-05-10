def powerset(arr,i=0):
    if len(arr) <= i:
        return [[]]
    assert len(arr) > i
    res = []
    for sub in powerset(arr, i+1):
        res.append(sub[:])
        res.append([arr[i]]+sub[:])
    return res
