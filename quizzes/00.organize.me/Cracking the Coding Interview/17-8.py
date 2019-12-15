'''
17.8 - 정수 배열이 주어진다(이 배열에는 양수 음수 모두 허용된다). 가장 큰 합을 갖는연속 수열을 찾고 그 합을 반환하라.
'''

sample_sequence = [2, -8, 3, -2, 4, -10]

def init_max_range(arr):
    return (0,1,arr[0])

def combination_idx(arr):
    for l in range(1, len(arr)+1):
        i = 0
        j = l
        while j <= len(arr):
            yield (i,j)
            i += 1
            j += 1

def max_in_sequence(arr):
    max_range=init_max_range(arr)
    for i,j in combination_idx(arr):
        s = sum(arr[i:j])
        if max_range[-1] < s:
            max_range = (i, j, s)
    return max_range

def main():
    i,j,val = max_in_sequence(sample_sequence)
    print("{}({}의 합)".format(val, sample_sequence[i:j]))

main()
