'''
10.1-정렬된 배열 A와 B가 주어진다. A의 끝에는 B를 수용하기 충분한 여유
공간이 있다. B와 A를 정렬된 상태로 병합하는 메서드를 작성하라.
'''
x=[1,3,5,7,9,None,None,None,None,None]
y=[2,3,6,8,9]
i=4
j=4
k=9

while k>=0:
#while i>=0 or j>=0:
    if j<0:
        #이미 정리 다됨
        break
    elif i<0:
        #다 위로 옮김
        while j>=0:
            x[k]=y[j]
            k-=1
            j-=1
    elif x[i]>=y[j]: #i,j >= 0
        x[k]=x[i]
        k-=1
        i-=1
    elif x[i]<y[j]:
        x[k] = y[j]
        k-=1
        j-=1
    else:
        assert False

print(x)
