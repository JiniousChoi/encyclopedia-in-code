
def initArray(ar, rows, colms):
    for i in range(rows):
        ar.append([])
        for j in range(colms):
            ar[i].append([])
    return ar

def rotateIndex(sizei, sizej, i, j, angle):
    i0,j0 = (float(sizei-1)/2, float(sizej-1)/2)
    
    if (angle=='270'):
        it, jt = -(j-j0), i-i0
    elif (angle=='180'):
        it, jt = -(i-i0), -(j-j0)
    elif (angle=='90'):
        it, jt = j-j0, -(i-i0)
    elif (angle=='360'):
        return i,j
    else:
        print 'Not supported'
        return
    
    return int(i0+it), int(j0+jt)

def getSizes(array):
    sizei = len(array)
    for row in array:
        sizej = len(row)
    return sizei, sizej
        
def rotateArray(ar_old, angle):
    sizei, sizej = getSizes(ar_old)
    ar_new = []
    initArray(ar_new, sizei, sizej)
    
    for i_old in range(sizei):
        for j_old in range(sizej):
            i_new, j_new = rotateIndex(sizei, sizej, i_old, j_old, angle)
            ar_new[i_new][j_new].append( ar_old[i_old][j_old][0] )
    return ar_new



sizei=sizej=5

array1 = []
array1 = initArray(array1, sizei, sizej)
x = 1
for i in range(sizei):
    for j in range(sizej):
        array1[i][j].append(x)
        x+=1

array2 = rotateArray(array1, '90')
array3 = rotateArray(array1, '180')
array4 = rotateArray(array1, '270')
array5 = rotateArray(array1, '360')
#print part
import pprint
print 'original'
pprint.pprint(array1)
print 'rotate 90'
pprint.pprint(array2)
print 'rotate 180'
pprint.pprint(array3)
print 'rotate 270'
pprint.pprint(array4)
print 'rotate 360'
pprint.pprint(array5)
