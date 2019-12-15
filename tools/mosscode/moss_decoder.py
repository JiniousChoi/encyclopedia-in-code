#!/usr/env python
# use python3

moss_code = "01 1000 1010 100 01 0010 110 0000 00 0111 101 0100 11 10 111 0110 1101 010 000 1 001 0001 011 1001 1011 1100"
moss_code = moss_code.split()
assert len(moss_code) == 26

alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabets = list(alphabets)
assert len(alphabets) == 26

MOSS = list(zip(moss_code, alphabets))
assert len(MOSS) == 26


def decoder(trys, code):

    if len(code) == 0:
        yield trys

    else:
        for alpha, code_left in resolve(code):
            yield from decoder(trys+[alpha], code_left)


def resolve(code):
    global MOSS

    for c,a in MOSS:
        if code.startswith(c):
            code_left = code[len(c):]
            yield (a, code_left)


def solution1(code):

    d = decoder([], code)

    for r in d:
        print(r)
        input()

def i_decoder(trys, code):
    ''' e) ['r','m','x'], code_left = i_decoder("i am hacke", "010011...")
        @trys :: "i am hacke ..."
        @code :: "0101100..."
        @return :: ([next_char], left_code)
    '''

    for a in trys:
        code = digest(a, code)
    
    next_chars = [a for a,c in resolve(code)]
    return (next_chars ,code)
    
def digest(a, code):
    ''' @return :: code_left '''
    c = a_to_c(a)
    if not code.startswith(c):
        raise Exception()

    return code[len(c):]

def a_to_c(a):
    global alphabets, moss_code

    A = a.upper()
    i = alphabets.index(A)
    c = moss_code[i]
    return c


def solution2(code):
    
    while(True):
        trys = input("> ")
        try:
            trys = trys.replace(' ', '')
            next_chars, code_left = i_decoder(trys, code)
            print(next_chars, code_left)
        
        except Exception:
            print("ERROR")


if __name__ == "__main__":
    code = "00011000000000" "10111110011101" "11111100010000" "11010101"

    #solution1(code)

    solution2(code)
    #i wish you good luck
