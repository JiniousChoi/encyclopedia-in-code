import math
def d(n):
    sum = 0
    howmanydigits = len(str(n))
    #sum of each digit
    for i in range( howmanydigits ):
        j = pow(10,i)
        j = int(j)
        sum+= ( n / j )%10
    sum += n
    return sum

summary = sum ( filter ( lambda x: x<5000 ,map( d, range(5000) ) ) )
print 'sum of self-numbers that are under 5000'
print 5000/2*5001 - summary
