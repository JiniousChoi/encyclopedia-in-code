#!/usr/bin/python3
from random import randint


def randhex():
    i = randint(0,255)
    return bytes([i])


def divider1(fname):
    divisor = 2
    
    fp1 = open(fname, 'rb')
    fp2 = open(fname+'.out1', 'wb')
    fp3 = open(fname+'.out2', 'wb')
    
    i = 0
    c = fp1.read(1)
    while c:
        if(i%divisor==0):
            fp2.write(c)
        else:
            fp2.write(randhex())
        c = fp1.read(1)
        i+=1

    fp2.close()

    i = 0
    fp1.seek(0)
    c = fp1.read(1)
    while c:
        if(i%divisor==1):
            fp3.write(c)
        else:
            fp3.write(randhex())
        c = fp1.read(1)
        i+=1

    fp3.close()
    fp1.close()


def swapper1(fname):
    pivot = 0b10101010
    
    fp1 = open(fname, 'rb')
    fp2 = open(fname+'.out1', 'wb')
    fp3 = open(fname+'.out2', 'wb')
    
    c = fp1.read(1)
    while c:
        ec = encrypt(c, pivot)
        fp2.write(ec)
        dec = encrypt(ec, pivot)
        fp3.write(dec)
        c = fp1.read(1)

    fp3.close()
    fp2.close()
    fp1.close()


def encrypt(_bytes, pivot):
    ''''''
    assert len(_bytes)==1
    return bytes([_bytes[0] ^ pivot])


def encrypt_file(fname, passphrase):
    UNIT=8 # 8bits per byte
    bitkey = ''.join([bin(ord(c)).lstrip('0b').zfill(UNIT) for c in passphrase])
    keysize, remainder = divmod(len(bitkey),UNIT)

    #import pdb; pdb.set_trace()
    assert remainder == 0
    #assert is_multiple_of_two(keysize)
    pivot = int(bitkey, 2)
    key_in_bytes = convert_to_bytes(pivot, UNIT)
    
    fp1 = open(fname, 'rb')
    fp2 = open(fname+'.out1', 'wb')
    
    bits = fp1.read(keysize)
    while bits:
        ec = encrypt_mbitwise(bits, key_in_bytes)
        fp2.write(ec)
        bits = fp1.read(UNIT)

    fp2.close()
    fp1.close()


def convert_to_bytes(integer, bytes_size):
    '''returns bytes that is converted from given integer'''
    result = bytearray()
    src = bin(integer).lstrip('0b').zfill(bytes_size*8)
    for i in range(0, len(src), 8):
        _int = int(src[i:i+8],2)
        result.append(_int)
    return bytes(result)
    
    
def encrypt_mbitwise(bytes, key_in_bytes):
    '''returns encrypted bytes in type of bytearray'''
    return bytearray([a^b for a,b in zip(bytes, key_in_bytes)])
    

def is_multiple_of_two(n):
    '''returns true if n is multiple of two, else false'''
    return 0 <= bin(n).count('1') <= 1


if __name__=="__main__":
    import sys
    fname = sys.argv[1]
    encrypt_file(fname, '루이보스보리차!@#')
    #encrypt_file(fname, 'password')
    #encrypt_file(fname, 'password1')
