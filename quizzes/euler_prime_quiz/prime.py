#!/usr/bin/env

from math import sqrt

fp = open('./euler.txt', 'r')
euler = fp.readline().strip()[2:] #remove 2.7

def get_euler(fr, to):
    global euler
    if fr <= to <= len(euler):
        return euler[fr:to]
    #append if possible
    line = fp.readline()
    if(line):
        euler = euler + line.strip()
        return get_euler(fr, to)

    #doom!
    return None

def test_get_euler():
    for i in range(100):
        ee = get_euler(i, i+10)
        print(ee)

def is_prime(n):
    for i in range(2, int(sqrt(n))+1):
        if(n%i==0): return False
    else:
        return True

def main():
    for i in range(0,500):
        x = get_euler(i, i+10)
        x = int(x)

        if(len(str(x))!=10): continue

        if( is_prime(x) ):
            print("")
            print("prime: ", x)
        else:
            print('.', sep="", end="")

if __name__ == '__main__':
    main()
    
    #test_get_euler()

#close always
fp.close()
