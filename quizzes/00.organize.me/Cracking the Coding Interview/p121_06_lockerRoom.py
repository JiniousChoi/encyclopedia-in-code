def quiz_lockerRoom(arr):
    box_cnt = len(arr)

    for i in range(box_cnt)[1::]:
        for j in range(box_cnt)[::i]:
            flipper(arr, j)
    return

def flipper(arr, i):
    if arr[i]==True:
        arr[i] = False
    elif arr[i] == False:
        arr[i] = True
    else:
        assert(False)
if __name__=="__main__":
    arr = [False]*101
    print arr[1:]
    fn(arr)
    print arr[1:]
    print arr[1:].count(True)


