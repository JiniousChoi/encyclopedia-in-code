def paintFill(arr, idx_x, idx_y, color_val_to, isSatisfyColorThrashHold):
    image_len_x = len(arr)
    image_len_y = len(arr[0])
    
    # 0<= idx_x < image_len_x
    # 0<= idx_y < image_len_y
    if 0> idx_x or idx_x>= image_len_x or 0> idx_y or idx_y>=image_len_y:
        assert(False)
    
    color_val_from = arr[idx_x][idx_y]
    #color_val_to = color_val_to
    
    queue = []
    #This won't let this function to repaint a stained picture to a solid color
    #if color_val_to != color_val_from:
        #queue.append((idx_x,idx_y))

    #On the other hand, no if as above, this can paint similar pixels around to a solid color
    queue.append((idx_x,idx_y))
    
    while( 0< len(queue) ):
        cur_idx_x, cur_idx_y = queue.pop(0)
        arr[cur_idx_x][cur_idx_y] = color_val_to
        
        ##enqueue part
        #left pixel
        if 0<cur_idx_y and isSatisfyColorThrashHold( color_val_from, arr[cur_idx_x][cur_idx_y-1] ):
            queue.append( (cur_idx_x,cur_idx_y-1) )
        
        #up pixel
        if 0< cur_idx_x and isSatisfyColorThrashHold( color_val_from, arr[cur_idx_x-1][cur_idx_y] ):
            queue.append( (cur_idx_x-1,cur_idx_y) )
        
        #right pixel
        if cur_idx_y<image_len_y-1 and isSatisfyColorThrashHold( color_val_from, arr[cur_idx_x][cur_idx_y+1] ):
            queue.append( (cur_idx_x,cur_idx_y+1) )
        
        #down pixel
        if cur_idx_x<image_len_x-1 and isSatisfyColorThrashHold( color_val_from, arr[cur_idx_x+1][cur_idx_y] ):
            queue.append( (cur_idx_x+1,cur_idx_y) )
            
    #end of while
    #no more pixels to color
    return

def isSatisfyColorThrashHold( color_val_from, proving_pixel):
    if color_val_from == proving_pixel:
        return True
    else:
        return False
    
def printArr(arr):
    for line in arr:
        print line
        
if __name__ == "__main__":

    arr1 = [
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    ]
    arr2 = [
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,1,1,0,0],
        [0,0,0,0,0,1,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,1,1,0,0],
        [0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
        [0,0,0,0,0,1,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    ]
    arr3 = [
        [1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1],
        [0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1],
        [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0],
        [0,1,2,3,4,5,6,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    ]
    def testcase1():
        print 'original'
        printArr( arr1 )
        paintFill(arr1, 5, 10, 2, isSatisfyColorThrashHold )
        print 'result'
        printArr( arr1 )

    def testcase2():    
        print 'original'
        printArr( arr2 )
        paintFill(arr2, 1, 14, 2, isSatisfyColorThrashHold )
        print 'result'
        printArr( arr2 )

    def testcase3():    
        print 'original'
        printArr( arr3 )
        paintFill(arr3, 0, 0, 7, isSatisfyColorThrashHold )
        paintFill(arr3, 1, 0, 4, isSatisfyColorThrashHold )
        paintFill(arr3, 2, 9, 8, isSatisfyColorThrashHold )
        print 'result'
        printArr( arr3 )
    import profile
    profile.run( 'testcase1()' )
