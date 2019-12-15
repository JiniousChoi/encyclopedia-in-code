#!/usr/bin/python3
## author: jinchoiseoul@gmail.com


def parse_io(inp, out):
    ''' io means input/output for testcases; 
        It splitlines them and strip the elements 
        @param inp: multi-lined str
        @param out: multi-lined str
        @return (inp::[str], out::[str])  '''
    inp = [i.strip() for i in inp.splitlines() if i.strip()]
    out = [o.strip() for o in out.splitlines() if o.strip()]
    return inp, out


def joiner(iterable, sep=' '):
    ''' @return e.g. [1, 2] -> "1 2" '''
    return sep.join(map(str, iterable))


def strips(doc):
    ''' @return strip each line of doc '''
    return '\n'.join(line.strip() for line in doc.splitlines())

    
def lstrips(doc):
    ''' @return lstrip each line of doc '''
    return '\n'.join(line.lstrip() for line in doc.splitlines())

def rstrips(doc):
    ''' @return rstrip each line of doc '''
    return '\n'.join(line.rstrip() for line in doc.splitlines())

