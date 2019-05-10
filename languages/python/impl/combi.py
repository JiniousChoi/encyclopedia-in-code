def combi(arr, cnt, i=0):
    if not(0 <= cnt <= len(arr)-i) or not (0 <= i <= len(arr)):
        return [] 
    assert i <= len(arr) and cnt <= len(arr)-i
    if cnt==0: 
        return [[]] 
    assert cnt > 0 and i < len(arr)
    res = [] 
    for sub in combi(arr, cnt-1, i+1):
        res.append([arr[i]]+sub[:])
    for sub in combi(arr, cnt, i+1):
        res.append(sub[:])
    return res
