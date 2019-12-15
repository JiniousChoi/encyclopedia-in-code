def getIntRotatedSequence(arr, find):

    left = 0
    right = len(arr)-1

    #okay: if arr[left] >= arr[right]:
    if arr[left] < arr[right]:
        assert(False)
    
    if arr[left] == find:
        return left
    elif arr[right] == find:
        return right

    #case: 5,6,7,[8],1,2,3,4    
    if arr[left] < find:
        while(1<right-left):
            mid = (left + right) / 2
            if arr[mid] == find:
                return mid
                
            elif arr[left] < find < arr[mid]:
                right = mid
            
            elif arr[mid] < arr[right]:
                right = mid

            else:
                left = mid
        
    #case: 5,6,7,8,1,[2],3,4
    elif find < arr[right]:
        while(1<right-left):
            mid = (left + right) / 2
            if arr[mid] == find:
                return mid
                
            elif arr[mid] < find < arr[right]:
                left = mid
            
            elif arr[mid] > arr[right]:
                left = mid
            
            elif find<arr[mid]:
                right = mid
                
            else:
                assert(False)
        
    else:
        assert(False)
    
    #end of if-else
    return -1
    
    
    
if __name__=="__main__":
    arr = [15,16,19,20,25,1,3,4,5,7,10,14]
    
    for i in [1,3,4,5,7,10,14, 8, 26, 17, 13 ,100]:
    #for i in [15,16,19,20,25]:
        print getIntRotatedSequence(arr, i)
