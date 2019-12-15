def counter(n):
    cnt = 0
    for i in range(n):
        cnt += howMany8s(i)
    return cnt

def howMany8s(num):
    if num < 0:
        assert(False)
    
    cnt = 0    
    
    while(0 < num):
        if (num%10) == 8:
            cnt+=1
        num/=10
    
    return cnt

if __name__=="__main__":
    print counter(10000)
