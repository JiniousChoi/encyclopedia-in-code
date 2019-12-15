'''
17.7 - 주어진 정수를 여엉로 변환하여 출력하라(One Thousand나 Two Hundred Thirty Four와 같이 출력하면 된다).
'''

units = ['', 'thousand', 'million', 'billion']
num_map = {
    1:'one',
    2:'two',
    3:'three',
    4:'four',
    5:'five',
    6:'six',
    7:'seven',
    8:'eight',
    9:'nine',
    10:'ten',
    11:'eleven',
    12:'twelve',
    13:'thirteen',
    14:'fourteen',
    15:'fifteen',
    16:'sixteen',
    17:'seventeen',
    18:'eighteen',
    19:'nineteen',
    20:'twenty',
    30:'thirty',
    40:'fourty',
    50:'fifty',
    60:'sixty',
    70:'seventy',
    80:'eighty',
    90:'ninety',
    100:'one hundred',
    200:'two hundred',
    300:'three hundred',
    400:'four hundred',
    500:'five hundred',
    600:'six hundred',
    700:'seven hundred',
    800:'eight hundred',
    900:'nine hundred',
}
def From1To999(num):
    assert isinstance(num, int)
    
    global num_map
    if num in num_map:
        return num_map[num]

    word = ''
    first, rest = bi_parting(num)
    word += num_map[first]
    word += ' '
    word += From1To999(rest)
    return word

def bi_parting(num):
    '''
    num_map에 없기때문에 둘로 쪼갬.
    '''
    assert 0<=num<1000
    global num_map
    assert num not in num_map

    numstr = str(num)
    first = int(numstr[0]+'0'*(len(numstr)-1))
    rest = int(numstr[1:])
    assert isinstance(first, int) and isinstance(rest, int)
    assert first!=0 and rest!= 0
    return first, rest

def number_teller(num):
    assert 0<= num <= 999999999999
    if num==0:
        return 'zero'
    chunks = grouping_by_n_digits(num)
    words = []
    for i,chunk in enumerate(chunks):
        if not chunk:
            continue
        words.append(From1To999(chunk))
        words.append(units[len(chunks)-1-i])
    return ' '.join(words)

def grouping_by_n_digits(num, n=3):
    '''
    3자리씩 잘라, 숫자의 리스트를 반환
    '''
    result = []
    numstr = str(num)
    padding_len = (n-len(numstr)%n)%n
    if padding_len:
       numstr=numstr.zfill(len(numstr)+padding_len) 

    assert len(numstr)%3==0
        
    while numstr:
        result.append(int(numstr[:3]))
        numstr = numstr[3:]
    return result
        


#def grouping_by_n_digits(num, n=3):
#    '''
#    3자리씩 잘라, 숫자의 리스트를 반환
#    '''
#    result = []
#    numstr = str(num)
#    while True:
#        if len(numstr)>=n:
#            numstr, end = numstr[:-n], numstr[-n:]
#            result.insert(0, int(end))
#        else:
#            result.insert(0, int(numstr))
#            break
#
#    return result
#

def main():
    sample_numbers = [0,1,7,17,33,97,100,119,199,200,500,1000, 1011, 1919, 9999, 10000, 99999, 100000, 999999, 1000000, 99999999]
    for number in sample_numbers:
        print(number_teller(number))

main()
