count = 0

def hanoiTower(arr, fromPoint, toPoint, howmany):
    if howmany<=0:
        return
        
    if howmany ==1:
        stone = arr[fromPoint].pop(0)
        arr[toPoint].insert(0, stone)
        global count 
        count +=1
        print count, 'th :', arr
        return
    
    detourPoint = getDetourPoint(fromPoint, toPoint)
    howmany -=1
    
    hanoiTower(arr, fromPoint, detourPoint, howmany)
    hanoiTower(arr, fromPoint, toPoint, 1)
    hanoiTower(arr, detourPoint, toPoint, howmany)

def getDetourPoint(fromPoint, toPoint):
    points = [0,1,2]
    total = sum(points)
    detourPoint = total - (fromPoint + toPoint)
    return detourPoint

def testcase1():
    assert(getDetourPoint(0,1) == 2)
    assert(getDetourPoint(0,2) == 1)
    assert(getDetourPoint(1,0) == 2)

    assert(getDetourPoint(1,2) == 0)
    assert(getDetourPoint(2,0) == 1)
    assert(getDetourPoint(2,1) == 0)

def testcase2():
    howmany = 5
    startpoint = 0
    endpoint = 2
    arr = [ range(howmany), [], [] ]
    print 'original :', arr
    hanoiTower(arr, startpoint, endpoint , howmany)
    print 'moved    :',arr
    assert ( arr == [ [],[],range(howmany) ] )
if __name__=='__main__':
    testcase1()
    testcase2()
