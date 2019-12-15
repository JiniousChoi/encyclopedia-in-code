#p149 10.6

def fn( the_val ,arr, top, left, bottom, right, result ):
    #if findOne==True:
        #return
    if top>bottom or left>right:
        return
        
    center_x = (top+bottom)/2
    center_y = (left+right)/2
    
    if arr[center_x][center_y] == the_val:
        result.append( (center_x, center_y) )
        #to top-left
        fn(the_val, arr, top, left, center_x-1, center_y-1, result)
        #to bottom-right
        fn(the_val, arr, center_x+1, center_y+1, bottom, right ,result)
        #to  left
        fn(the_val, arr, center_x, left, center_x, center_y-1, result)
        #to right
        fn(the_val, arr, center_x, center_y+1, center_x, right, result)
        #to top
        fn(the_val, arr, top, center_y, center_x-1, center_y, result)
        #to bottom
        fn(the_val, arr, center_x+1, center_y, bottom, center_y, result)

    elif arr[center_x][center_y] > the_val:
        #to top-left
        fn(the_val, arr, top, left, center_x-1, center_y-1, result)
        #to left
        fn(the_val, arr, center_x, left, center_x, center_y-1, result)
        #to top
        fn(the_val, arr, top, center_y, center_x-1, center_y, result)
        
    elif arr[center_x][center_y] < the_val:
        #to bottom-right
        fn(the_val, arr, center_x+1, center_y+1, bottom, right ,result)
        #to bottom
        fn(the_val, arr, center_x+1, center_y, bottom, center_y, result)
        #to right
        fn(the_val, arr, center_x, center_y+1, center_x, right, result)
    else:
        assert(False)
    
    ##common part
    #to top-right
    fn(the_val, arr, top, center_y+1, center_x-1, right, result)
    #to bottom-left
    fn(the_val, arr, center_x+1, left, bottom, center_y-1, result)
    
def fn_wrapper( the_val, arr ):
    first_line = arr[0]
    for nth_line in arr[1:]:
        if len(first_line) != len(nth_line):
            print 'not a matrix'
            return []
    top = 0
    left = 0
    bottom = len(arr) - 1
    right = len(first_line) - 1
    
    result = []
    fn( the_val, arr, top, left, bottom, right, result )
    return result

if __name__ == "__main__":

    test_arr = [
        [1,2,3,4,5,6],
        [3,4,4,4,6,8],
        [5,5,5,5,9,11],
        [5,6,7,8,12,15],
        [8,11,16,18,20,22],
    ]
    #test_arr = [[1,2,3],[4,5,6],[7,8,9]]
    
    for the_val in range(22):
        result = fn_wrapper( the_val, test_arr )
        print result
    
