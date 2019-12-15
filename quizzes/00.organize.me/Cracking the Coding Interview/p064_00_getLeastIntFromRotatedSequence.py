#page 64
#Done perfectly!!
def getLeastIntFromRotatedSequence(ls):
    left=0
    right=len(ls)-1
    if ( ls[left] < ls[right] ):
        return ls[0]
        
    while(right-left != 1):
        mid = (left+right) / 2
        if( ls[left] <= ls[mid] ):
            left = mid
        else:
            right = mid
    #out of loop, right must be the index of the least int
    return ls[right]

test_ls= [ [3,4,5,6,7,-11,2],
                [5,6,7,3,4,5,5,5],
                [1,2],
                [2,1],
                [-100,0,100],
                [3,100,1],
                [10,1,2,3,4,5,6,7,8,9],
                [2,3,4,5,6,7,8,9,10,1] ]

#test part
for each_list in test_ls:
    print getLeastIntFromRotatedSequence( each_list )
