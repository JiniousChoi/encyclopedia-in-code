#explain what the following code does: (( n & (n-1)) == 0 )
def tester(range_from, range_to):
    for n in range(range_from, range_to+1):
        if (( n & (n-1)) == 0 ):
            print n,

if __name__=="__main__":
    tester(-1000, 10000)

#0 1 2 4 8 16 32 64 128 256 512 1024 2048 4096 8192
