import pdb

class MinHeap:
    def __init__( self, size ):
        self.size = size+1
        self.cnt = 0
        self.heap = []
        for i in range(self.size):
            self.heap.append([])
    
    def getParentIdx ( self, idx ):
        return idx/2
    
    def getLeftChildIdx( self, idx ):
        return 2*idx

    def getRightChildIdx( self, idx ):
        return 2*idx+1
    
    def addInt( self, num ):
        if self.cnt > self.size-2:
            return False
        
        self.cnt += 1
        self.heap[self.cnt] = [num]
        
        #process to keep in order
        my_idx = self.cnt
        while(my_idx > 1):
            par_idx = self.getParentIdx(my_idx)
            
            if self.heap[ par_idx ] > self.heap[ my_idx ]:
                self.heap[ par_idx ], self.heap[ my_idx ] =  self.heap[ my_idx ], self.heap[ par_idx ]
            my_idx = par_idx
        
        return True
    
    def popHeap( self ):
        if self.cnt<1:
            return None
        #save return value in the end
        min_val = self.heap[1][:]
        rpl_val = self.heap[self.cnt][:]
        self.cnt -= 1
        emt_idx = 1
        
        while(True):
            #if right child exists, both children exist:
            if self.getRightChildIdx(emt_idx) <= self.cnt:
                l_idx, r_idx = self.getLeftChildIdx(emt_idx), self.getRightChildIdx(emt_idx)
                
                #get the least value and its index
                if self.heap[l_idx] < self.heap[r_idx] :
                    the_idx = l_idx
                    the_val = self.heap[l_idx]
                else:
                    the_idx = r_idx
                    the_val = self.heap[r_idx]
                
                #check if heap is out of order:
                if the_val < rpl_val:
                    self.heap[emt_idx] = the_val
                    emt_idx = the_idx
                #if heap is in order:
                else:
                    self.heap[emt_idx] = rpl_val
                    break
            
            #if right child doesn't exist and left child exists:
            elif self.getLeftChildIdx(emt_idx) <= self.cnt:
                l_idx = self.getLeftChildIdx(emt_idx)
                l_val = self.heap[l_idx]
                if l_val < rpl_val:
                    self.heap[emt_idx] = l_val
                    emt_idx = l_idx
                else:
                    self.heap[emt_idx] = rpl_val
                    break
            #if no child:
            else:
                self.heap[emt_idx] = rpl_val
                break
                
        #return the temporarily saved least value in the heap
        return min_val
    
    def PrintHeap( self ):
        print self.heap[1:self.cnt+1]
    ###
    ###End of Class
    ###
  
def unitTest1():
    minHeap = MinHeap(10)
    for i in [3,4,2,5,6,7,1,8]:
        minHeap.addInt(i)
    
    minHeap.PrintHeap()
    for i in range(5):
        minHeap.popHeap()
        minHeap.PrintHeap()
    
    for i in [1,22,3,4,55,-5]:
        minHeap.addInt(i)
    minHeap.PrintHeap()

    for i in range(7):
        print minHeap.popHeap()
    minHeap.PrintHeap()

def heapSort(arr):
    minHeap = MinHeap(len(arr))
    for i in arr:
        minHeap.addInt(i)
    
    result = []
    while(True):
        p = minHeap.popHeap()
        if p == None:
            break
        result.append(p[0])
    
    return result
    
if __name__=="__main__":
    arr = [3,4,2,5,6,7,1,8]
    print 'arr ->',
    print arr
    arr_sorted = heapSort(arr)
    print 'arr_sorted ->',
    print arr_sorted
    
