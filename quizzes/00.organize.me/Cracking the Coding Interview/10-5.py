'''
10.5 - 빈 문자열이 섞여 있는 정렬 상태의 배열이 주어졌을 때, 특정한 문자열 의 위치를 찾는 메서드를 작성하라.
'''

def search_arr_with_empty_string(arr, target):
    assert arr
    left = init_left(arr)
    right = init_right(arr)
    mid = get_mid(arr, left, right)

    while mid>=0:
        if arr[mid]==target:
            return mid

        if arr[mid]>target:
            right=mid
        elif arr[mid]<target:
            left=mid
        else:
            assert False
        mid = get_mid(arr, left, right)
    return -1

def init_left(arr):
    for i,e in enumerate(arr):
        if e:
            return i
    raise Exception("주어진 배열이 빈문자열로만 차있습니다")

def init_right(arr):
    for i in range(len(arr)-1, -1, -1):
        if arr[i]:
            return i
    raise Exception("주어진 배열이 빈문자열로만 차있습니다")

def get_mid(arr, left, right):
    assert left < right
    mid = (left+right)//2
    if arr[mid]:
        return mid

    for t in range(mid-1, left, -1):
        if arr[t]:
            return t

    for t in range(mid+1, right):
        if arr[t]:
            return t

    return -1

sample_arr = ["at","","","","ball","","","car","","","dad","",""]
idx = search_arr_with_empty_string(sample_arr, "ball")
print(idx)
